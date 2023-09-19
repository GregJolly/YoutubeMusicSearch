from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import pygame 

pygame.init()

# Create a Pygame window for user input
width, height = 400, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("YouTube Song Player")

def ask_query():
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(50, 50, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
pygame.display.update()
pygame.quit()
def ask_query():
    search_input = input("What song do you want to listen to (Artist - The song): ")
    return search_input

def open_youtube(query):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/results?search_query="+query)
    return driver
    
def click_button_with_css(driver, css_selector):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    element.click()
    
def click_video(driver, search_input):
    click_css = '[aria-label*="'+ search_input +'"]'
    click_button_with_css(driver, click_css)
    
def skip_button(driver):
    skip_css = '[class*="ytp-ad-skip-button ytp-button"]'
    click_button_with_css(driver, skip_css)
    
def main():
    search = ask_query()
    if search:
        query = search.replace(' ', '+')
        driver = open_youtube(query)
        time.sleep(2)
        click_video(driver, search)
        time.sleep(2)
        skip_button(driver)
        time.sleep(1000)
    
main()