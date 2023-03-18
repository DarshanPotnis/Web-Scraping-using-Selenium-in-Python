#Importing Libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

# Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server, marks a leap forward in terms of browser automation.
# Creating WebDriver instance
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Get the main page
wd.get("https://www.wikipedia.org/")

# Assertion Statement
assert "Wikipedia" in wd.title

# Print the entire HTML
#print(wd.page_source)

# Fetching the element by ID
input_element = wd.find_element(by = By.ID, value = "searchInput")

# Sending keys
input_element.send_keys('ASD')

# Fetch search button through CSS class name
search = wd.find_element(by=By.CLASS_NAME, value="pure-button")

# Click the search button
wd.execute_script("arguments[0].click();", search)

# Switching windows
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# Assertion statement
assert "ASD - Wikipedia" in wd.title

# Printing the title
print("Successfully loaded the page", wd.title)

# Fetch search button through link text
link_text = wd.find_element(By.LINK_TEXT, "Adaptive software development")

# Clicking the link
wd.execute_script("arguments[0].click();", link_text)

# Switching window
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# Assertion statement
assert "Adaptive software development - Wikipedia" in wd.title

# Printing the title
print("Successfully loaded the page ",wd.title)

# Fetch all elements with <p> tags
p_tags = wd.find_elements(by=By.TAG_NAME, value="p")

# Printing the array with <p> tag elements
print("Number of tags found: ",len(p_tags))

text_lines = ''

for p_tag in p_tags:
    text_lines = text_lines + p_tag.text

# Print the text
print(text_lines)

# Match all digits occuring in squared brackets in the string and replace them with an empty string
pattern = r'\[[0-9]\]'
new_string = re.sub(pattern, '', text_lines)
print(new_string)

elems= wd.find_elements(by=By.CSS_SELECTOR, value='p > a')

# Creating Dictionary
link_dict = {}
for elem in elems:
    link_dict[elem.text] = elem.get_attribute('href')
print(link_dict)