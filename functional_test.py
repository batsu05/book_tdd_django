from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_row_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('To-Do',self.browser.title)

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'input item')

		inputbox.send_keys('buy feather')
		inputbox.send_keys(Keys.ENTER)

		'''

		# import time
		# time.sleep(10)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')

		#self.assertIn('1: buy feather', [row.text for row in rows])

		#self.assertTrue(
		#	any(row.text == '1: buy feather' for row in rows), "no items in table")

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('making net with feather')
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')

		self.assertIn('1: buy feather', [row.text for row in rows])
		self.assertIn('2: making net with feather', [row.text for row in rows])
		'''

		
		#inputbox.send_keys(Keys.ENTER)
		self.check_row_list_table('1: buy feather')

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('making net with feather')
		inputbox.send_keys(Keys.ENTER)

		self.check_row_list_table('2: making net with feather')
		self.check_row_list_table('1: buy feather')

		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main()