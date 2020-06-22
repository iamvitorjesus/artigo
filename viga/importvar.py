from app.template import newproject.html


newproject =
elements = newproject.find_by_css("#mydiv")
div = elements[0]
print div.value

browser.quit()
