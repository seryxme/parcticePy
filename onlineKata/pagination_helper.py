class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if self.item_count() % self.items_per_page != 0:
            return (self.item_count() // self.items_per_page) + 1

        return self.item_count() // self.items_per_page

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if 0 <= page_index < self.page_count():
            if not page_index == self.page_count() - 1:
                return self.items_per_page
            else:
                return self.item_count() % self.items_per_page

        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if 0 <= item_index < self.item_count():
            return item_index // self.items_per_page

        return -1


# collection = range(1,25)
# helper = PaginationHelper(collection, 10)
#
# print(helper.page_count(), " expecting 3")
# print(helper.page_index(23), " expecting 2")
# print(helper.item_count(), " expecting 24")