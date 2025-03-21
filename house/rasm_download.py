from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Selenium WebDriver yuklab olish
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Brauzerni fon rejimida ochish
driver = webdriver.Chrome(options=options)

try:
    # Stability AI saytiga kirish
    driver.get("https://stability.ai/")

    # Sayt yuklanishini kutish
    time.sleep(3)

    # Rasm yuklash tugmasini bosish
    upload_button = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    upload_button.send_keys(os.path.abspath("test.png"))  # Yuklanayotgan rasm

    # Generatsiyani boshlash
    generate_button = driver.find_element(By.XPATH, "//button[text()='Generate']")
    generate_button.click()

    # Natijani kutish
    time.sleep(10)

    # Natijani yuklab olish
    generated_image = driver.find_element(By.CSS_SELECTOR, "img.generated")
    image_url = generated_image.get_attribute("src")

    print("Generated Image URL:", image_url)

finally:
    driver.quit()


from django.http import JsonResponse

def generate_design(request):
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]

        # Stability AI saytiga avtomatik yuklash
        image_url = generate_image_via_website(image_file)

        return JsonResponse({"image_url": image_url})

    return JsonResponse({"error": "Rasm yuklanmadi!"}, status=400)
