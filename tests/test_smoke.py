import logging

logger = logging.getLogger(__name__)


def test_open_demoqa_and_fail(page):
    page.goto("https://demoqa.com/")

    logger.info('\nExpecting page title as: DEMOQA'
               f'\nActual page_title is: {page.title()}'
                '\nThe test should fail.')

    assert "DEMOQA" in page.title()

def test_open_demoqa_and_pass(page):
    page.goto("https://demoqa.com/")

    #logger.info(f'\nActual page_title is: {page.title()}')

    assert "demosite" in page.title()