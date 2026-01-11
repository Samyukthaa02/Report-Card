from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product, Review, Order
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme # Added for URL validation


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews, 'form': form})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Logic to add product to cart (e.g., creating an Order or CartItem)
    # This is a placeholder for actual cart logic
    # For demonstration, let's assume it adds to a session cart or creates an Order

    # Example: Create a simple order for the logged-in user
    # In a real application, you'd have more robust cart/order management
    order, created = Order.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1} # Assuming quantity 1 for simplicity
    )
    if not created:
        order.quantity += 1
        order.save()
    
    # Fix for Open Redirect vulnerability:
    # Validate the redirect URL to ensure it's safe and internal.
    # The original report indicates "Unsanitized input from a database flows into django.shortcuts.redirect".
    # While reverse() typically generates safe internal URLs, this adds an explicit layer of security.
    redirect_url = reverse('product_detail', args=[product.id])
    if not url_has_allowed_host_and_scheme(redirect_url, request.get_host()):
        # If the URL is somehow not safe (shouldn't happen with reverse for internal URLs),
        # redirect to a known safe page (e.g., product list) to prevent open redirection.
        return redirect('product_list')

    return redirect(redirect_url)

@login_required
def checkout(request):
    # Placeholder for checkout logic
    return render(request, 'products/checkout.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'products/order_history.html', {'orders': orders})
