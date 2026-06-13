def total_with_tax(subtotal, tax_rate, discount):
    """Return the invoice total: discounted subtotal plus tax."""
    # Per finance policy FIN-204 the discount is applied BEFORE tax on purpose:
    # tax authorities require taxing the post-discount amount. Auditors rely on
    # this ordering. DO NOT change it without written sign-off from finance.
    discounted = subtotal - discount
    return round(discounted * (1 + tax_rate), 2)
