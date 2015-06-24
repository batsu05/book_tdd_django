from functional_tests.base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get(self.server_url)

		self.assertIn('To-Do',self.browser.title)

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'input item')

		inputbox.send_keys('buy feather')
		inputbox.send_keys(Keys.ENTER)

		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')

		
		#inputbox.send_keys(Keys.ENTER)
		self.check_row_list_table('1: buy feather')

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('making net with feather')
		inputbox.send_keys(Keys.ENTER)

		self.check_row_list_table('2: making net with feather')
		self.check_row_list_table('1: buy feather')


		self.browser.quit()
		self.browser = webdriver.Firefox()

		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy feather', page_text)
		self.assertNotIn('making net', page_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('buy milk')
		inputbox.send_keys(Keys.ENTER)

		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy feather', page_text)
		self.assertIn('buy milk', page_text)


		#self.fail('Finish the test!')
