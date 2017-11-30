import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("samplexml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    skills = doc.getElementsByTagName("skill")
    print ("{} skills: ".format(skills.length))
    for skill in skills: 
        print (skill.getAttribute("name"))
    
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)
    print ("  ")
    
    skills = doc.getElementsByTagName("skill")

    for skill in skills: 
        print (skill.getAttribute("name"))
    
    
    
if __name__ == "__main__":
    main()