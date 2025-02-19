from playwright.sync_api import Page
from playwright_tests.core.testutilities import TestUtilities
from playwright_tests.pages.ask_a_question.product_solutions_pages.product_solutions_page import (
    ProductSolutionsPage)
from playwright_tests.pages.top_navbar import TopNavbar
from playwright_tests.pages.ask_a_question.aaq_pages.aaq_form_page import AAQFormPage
from playwright_tests.pages.ask_a_question.posted_question_pages.questions_page import QuestionPage


class AAQFlow(AAQFormPage, ProductSolutionsPage, TopNavbar, TestUtilities, QuestionPage):
    def __init__(self, page: Page):
        super().__init__(page)

    # Submitting an aaq question for a product flow.
    # Mozilla VPN has an extra optional dropdown menu for choosing an operating system.
    def submit_an_aaq_question_for_a_product(self,
                                             subject: str,
                                             topic_name: str,
                                             body: str,
                                             os="",
                                             attach_image=False):
        question_subject = self.add__valid_data_to_all_input_fields_without_submitting(
            subject,
            topic_name,
            body,
            os,
            attach_image
        )
        # Submitting the question.
        super()._click_aaq_form_submit_button()
        # Waiting for submitted question reply button visibility.
        super()._is_post_reply_button_visible()
        current_page_url = self._page.url

        # Returning the posted question subject and url for further usage.
        return {"aaq_subject": question_subject, "question_page_url": current_page_url,
                "question_body": body}

    # Populating the aaq form fields with given values without submitting the form.
    # Mozilla VPN has an extra optional dropdown menu for choosing an operating system.
    def add__valid_data_to_all_input_fields_without_submitting(self,
                                                               subject: str,
                                                               topic_value: str,
                                                               body_text: str,
                                                               os='',
                                                               attach_image=False):
        aaq_subject = subject + super().generate_random_number(min_value=0, max_value=1000)
        # Adding text to subject field.
        super()._add_text_to_aaq_form_subject_field(aaq_subject)
        # Selecting a topic.
        super()._select_aaq_form_topic_value(
            topic_value
        )
        # Adding text to question body.
        super()._add_text_to_aaq_textarea_field(
            body_text
        )
        # Some products contain another OS dropdown menu. We are selecting an option for those.
        if os != "":
            super()._select_aaq_form_os_value(os)

        if attach_image:
            # Uploading an image to the aaq question form.
            super()._get_upload_image_button_locator().set_input_files(
                super().aaq_question_test_data["valid_firefox_question"]["image_path"]
            )

            # Waiting for the image preview to be displayed.
            super()._uploaded_image_locator()

        # Returning the entered question subject for further usage.
        return aaq_subject

    # Adding an image to the aaq form.
    def adding_an_image_to_aaq_form(self):
        super()._get_upload_image_button_locator().set_input_files(
            super().aaq_question_test_data["valid_firefox_question"]["image_path"]
        )
