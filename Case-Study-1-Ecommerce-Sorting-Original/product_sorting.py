def payable_price(product):
    return round(product["list_price"] * (100 - product["discount_percent"]) / 100, 2)


def merge_sort_by_payable_price(products):
    if len(products) <= 1:
        return products, 0

    middle = len(products) // 2
    left, left_comparisons = merge_sort_by_payable_price(products[:middle])
    right, right_comparisons = merge_sort_by_payable_price(products[middle:])
    result = []
    left_index = 0
    right_index = 0
    comparisons = left_comparisons + right_comparisons

    while left_index < len(left) and right_index < len(right):
        comparisons += 1
        if payable_price(left[left_index]) <= payable_price(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result, comparisons


def sample_products():
    return [
        {"name": "Noise-Cancelling Headphones", "category": "Audio", "list_price": 4800, "discount_percent": 25, "rating": 4.7},
        {"name": "Canvas Backpack", "category": "Bags", "list_price": 3200, "discount_percent": 10, "rating": 4.5},
        {"name": "Desk Lamp", "category": "Home", "list_price": 1800, "discount_percent": 0, "rating": 4.2},
        {"name": "Coffee Grinder", "category": "Kitchen", "list_price": 4200, "discount_percent": 15, "rating": 4.6},
        {"name": "Water Bottle", "category": "Outdoor", "list_price": 1200, "discount_percent": 0, "rating": 4.4},
        {"name": "Running Shoes", "category": "Footwear", "list_price": 5000, "discount_percent": 20, "rating": 4.8},
        {"name": "Travel Organizer", "category": "Bags", "list_price": 2400, "discount_percent": 25, "rating": 4.3},
    ]


def display_products(title, products):
    print(title)
    for product in products:
        print(
            f"{product['name']:<30} | {product['category']:<9} | "
            f"List: Rs. {product['list_price']:>7.2f} | "
            f"Discount: {product['discount_percent']:>2}% | "
            f"Payable: Rs. {payable_price(product):>7.2f} | "
            f"Rating: {product['rating']:.1f}"
        )


def main():
    products = sample_products()
    sorted_products, comparisons = merge_sort_by_payable_price(products)

    print("E-COMMERCE: SORT BY CUSTOMER PAYABLE PRICE")
    display_products("\nCatalog before sorting:", products)
    display_products("\nCatalog after sorting (low to high):", sorted_products)
    print(f"\nPrice comparisons during merging: {comparisons}")


if __name__ == "__main__":
    main()
