import time
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.contact_cache = None

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

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_css_selector("input[id='%s']" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        time.sleep(1)
        self.return_to_home_page()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.get("http://localhost/addressbook/")

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(index=0, contact=contact)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        # нажатие на иконку редактирования контакта
        wd.find_elements_by_xpath("//a/img[@title='Edit']")[index].click()


    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_index(index)
        # редактирование всех полей
        self.fill_fields(contact)
        # submit edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        # нажатие на иконку редактирования контакта
        wd.find_element_by_css_selector("a[href $= 'id=%s'] img[title=Edit]" % id).click()

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_id(id)
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
                address = elm.find_element_by_xpath(".//td[4]").text
                all_emails = elm.find_element_by_xpath(".//td[5]").text
                all_phones = elm.find_element_by_xpath(".//td[6]").text
                self.contact_cache.append(Contact(id=contact_id, firstname=first_name, lastname=last_name,
                                                  address=address, all_emails_from_homepage=all_emails,
                                                  all_phones_from_homepage=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, homephone=homephone,
                       mobile=mobile, workphone=workphone, phone2=phone2, address=address,
                       email=email, email2=email2, email3=email3)
