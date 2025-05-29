from bs4 import BeautifulSoup

def load_html(file_path):  # Add file_path as parameter
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return content

def extract_persons(soup):
    persons = []
    person_elements=soup.find_all(name="div",class_="person")

    for person in person_elements:
        Name=person.find("h1").text
        City = person.find("h2").text
        Company = person.find("h3").text
        Designation = person.find("p").text

        #print(username,content,timestamp)
        persons.append({"Name":Name,"City":City,"Company":Company,"Designation":Designation})
    return persons

html_content = load_html("NewHtml.html")
soup = BeautifulSoup(html_content, "html.parser")

persons = extract_persons(soup)

for person in persons:
    print(f"Name:{person['Name']}")
    print(f"City:{person['City']}")
    print(f"Company:{person['Company']}")
    print(f"Designation:{person['Designation']}")
    print("--------------------------------------------------")

#html-soup object