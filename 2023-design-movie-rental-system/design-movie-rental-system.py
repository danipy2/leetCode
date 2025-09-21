class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.ava = {}  
        self.ms = {}  
        self.rented = set()  

        for shop, movie, price in entries:
            self.ava[(shop, movie)] = price
            if movie not in self.ms:
                self.ms[movie] = []
            self.ms[movie].append((price, shop))

        
        for movie in self.ms:
            self.ms[movie].sort()

    def search(self, movie: int) -> List[int]:
        result = []
        for price, shop in self.ms.get(movie, []):
            if (shop, movie) not in self.rented:
                result.append(shop)
            if len(result) == 5:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))

    def report(self) -> List[List[int]]:
        rented_list = []
        for shop, movie in self.rented:
            price = self.ava[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()
        return [[shop, movie] for price, shop, movie in rented_list[:5]]