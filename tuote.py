"""
Product

The program describes a simple class Product which can be used to handle
products available in a store. Every product has three properties:
- name (str)
- price (float)
- sale percentage (float)

The numbers are floats and printed with two decimals.

Writer of the program: EILeh

"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, product_name="Product",
                 normal_price = 0.00,
                 get_price = 0.00,
                 set_sale_percentage = 0.00):
        """
        A product object is initialized with the product name, normal price,
        reduced price and the sale percentage.
        :param product_name: str, the name of the product
        :param normal_price: float, product's normal price
        :param get_price: float, reduced price
        :param set_sale_percentage: float, the percentage which is reduced
        from normal price
        """

        # product's name
        self.__name = product_name

        # normal price without sale percentage
        self.__normal_price = normal_price

        # reduced price
        self.__sale_price = get_price

        # sale as a percent
        self.__percentage = set_sale_percentage

    def printout(self):
        """
        Prints the products name, normal price and sale percetage.
        """

        print(f"{self.__name}")
        print(f"  price: {self.__normal_price:.2f}")
        print(f"  sale%: {self.__percentage:.2f}")

    def set_sale_percentage(self, percentage):
        """
        Price after reduced percent.
        :param percentage: float, sale percent
        :return: returns the reduced price
        """

        self.__percentage = percentage
        self.__sale_price = self.__normal_price - (self.__normal_price * (self.__percentage / 100))
        return self.__sale_price

    def get_price(self):
        """
        Price after sale percentage.
        :return: returns normal price if sale percentage zero, otherwise
        returns reduced price
        """

        if self.__percentage <= 0.0:
            return self.__normal_price
        else:
            return self.__sale_price

def main():
    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

if __name__ == "__main__":
    main()
