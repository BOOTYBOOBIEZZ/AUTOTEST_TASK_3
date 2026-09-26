from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class AlertsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.js_alert_button = WebElement(
            locator=page.locator("button", has_text="Click for JS Alert"),
            description="Кнопка JS Alert",
            page=page,
        )
        self.js_confirm_button = WebElement(
            locator=page.locator("button", has_text="Click for JS Confirm"),
            description="Кнопка JS Confirm",
            page=page,
        )
        self.js_prompt_button = WebElement(
            locator=page.locator("button", has_text="Click for JS Prompt"),
            description="Кнопка JS Prompt",
            page=page,
        )

        self.result_text = WebElement(
            locator=page.locator("#result"),
            description="Текст результата",
            page=page,
        )

    def click_js_alert_button(self):
        return self.actions.run_and_accept_alert(
            action=lambda: self.js_alert_button.click()
        )

    def click_js_confirm_and_accept(self):
        """Кликает и принимает confirm."""
        return self.actions.run_and_accept_alert(
            action=lambda: self.js_confirm_button.click()
        )

    def click_js_confirm_and_dismiss(self):
        """Кликает и отклоняет confirm."""
        return self.actions.run_and_dismiss_alert(
            action=lambda: self.js_confirm_button.click()
        )

    def click_js_prompt_button(self, prompt_text: str):
        return self.actions.run_and_accept_prompt(
            action=lambda: self.js_prompt_button.click(),
            prompt_text=prompt_text,
        )

    def get_result_text(self) -> str:
        return self.actions.get_text(self.result_text)

    def wait_for_open(self):
        self.js_alert_button.locator.wait_for(state="visible")
