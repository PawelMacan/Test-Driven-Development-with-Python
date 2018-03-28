from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has hear about a coo new online to-do app. She goes
        #  to check out its home page

        self.browser.get('http://localhost:8000')

        # She notices the page title and header mantion to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacook feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add antoher item.
        # She enters "Use peacock feather to make a fly" She's very methodical

        # The page updates again, and now shows both items on her list

        # Edith wonders  whether the site will remember her list. Then she sees
        # That the site has generated a unique URL for her -- there is some
        # explanatory tehxt to that effect

        # She visits that URl - her to-do list is still there

        # Satisfied, she goes back to sleap


if __name__ == '__main__':
    unittest.main(warnings='ignore')
