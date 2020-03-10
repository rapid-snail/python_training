from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_add_new_page()
        self.fill_fields(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # возврат на страницу home page
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.get("http://localhost/addressbook/")

    def edit_first(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # нажатие на иконку редактирования первого контакта
        wd.find_element_by_xpath("//a/img[@title='Edit']").click()
        # редактирование всех полей
        self.fill_fields(contact)
        # submit edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_fields(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            elms = wd.find_elements_by_css_selector("tr[name='entry']")
            for elm in elms:
                contact_id = elm.find_element_by_name("selected[]").get_attribute("value")
                first_name = elm.find_element_by_xpath(".//td[3]").text
                last_name = elm.find_element_by_xpath(".//td[2]").text
                self.contact_cache.append(Contact(id=contact_id, firstname=first_name, lastname=last_name))
        return list(self.contact_cache)
