"""One-off assisted verification of the 12 complementary case definitions.

This executable protocol is archived with the evidence; the maintained Robot
regression suite remains the 12 scenarios under tests/ui.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, os, sys, traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from decimal import Decimal

BASE='https://www.saucedemo.com/'
OUT=Path('outputs/QA-Portfolio-SauceDemo/evidence/2026-10-16/complementary')
OUT.mkdir(parents=True,exist_ok=True)
os.environ['SE_CACHE_PATH']=str(Path('work/selenium-cache').resolve())
os.environ['SE_AVOID_STATS']='true'
records=[]
reference={
 'Sauce Labs Backpack':'$29.99', 'Sauce Labs Bike Light':'$9.99',
 'Sauce Labs Bolt T-Shirt':'$15.99', 'Sauce Labs Fleece Jacket':'$49.99',
 'Sauce Labs Onesie':'$7.99', 'Test.allTheThings() T-Shirt (Red)':'$15.99'}

def visible(name):
    return WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,f'[data-test="{name}"]')))
def click(name): visible(name).click()
def texts(name): return [e.text for e in driver.find_elements(By.CSS_SELECTOR,f'[data-test="{name}"]')]
def absent(name): assert not driver.find_elements(By.CSS_SELECTOR,f'[data-test="{name}"]'),name
def login():
    visible('username').send_keys('standard_user')
    visible('password').send_keys('secret_sauce')
    click('login-button'); visible('inventory-list')
def add(): click('add-to-cart-sauce-labs-backpack'); assert visible('shopping-cart-badge').text=='1'
def cart(): click('shopping-cart-link'); visible('cart-list')
def cart_one():
    assert texts('inventory-item-name')==['Sauce Labs Backpack']
    assert texts('inventory-item-price')==['$29.99']
    assert visible('shopping-cart-badge').text=='1'
def identity():
    visible('firstName').send_keys('Camille');visible('lastName').send_keys('Test');visible('postalCode').send_keys('75001')
def pairs():
    return [(e.find_element(By.CSS_SELECTOR,'[data-test="inventory-item-name"]').text,
             e.find_element(By.CSS_SELECTOR,'[data-test="inventory-item-price"]').text)
            for e in driver.find_elements(By.CSS_SELECTOR,'[data-test="inventory-item"]')]

def missing_username():
    visible('password').send_keys('secret_sauce');click('login-button')
    assert 'Username is required' in visible('error').text;visible('login-button')
    return 'Erreur Username is required ; formulaire de connexion conservé.'
def missing_password():
    visible('username').send_keys('standard_user');click('login-button')
    assert 'Password is required' in visible('error').text;visible('login-button')
    return 'Erreur Password is required ; formulaire de connexion conservé.'
def catalog_reference():
    login(); actual=pairs()
    assert len(actual)==6 and dict(actual)==reference and len(set(n for n,p in actual))==6
    for element in driver.find_elements(By.CSS_SELECTOR,'[data-test="inventory-item"]'):
        image=element.find_element(By.TAG_NAME,'img')
        assert driver.execute_script('return arguments[0].complete && arguments[0].naturalWidth > 0',image)
        assert element.find_element(By.TAG_NAME,'button').is_displayed()
    return 'Six produits uniques conformes à D-03 ; six images chargées et boutons visibles.'
def details():
    login();click('item-4-title-link')
    assert visible('inventory-item-name').text=='Sauce Labs Backpack'
    assert visible('inventory-item-price').text=='$29.99'
    click('back-to-products');visible('inventory-list');absent('shopping-cart-badge')
    return 'Fiche Backpack : nom/prix identiques ; retour catalogue et panier vide.'
def sort_prices_desc():
    login();before=pairs();Select(visible('product-sort-container')).select_by_value('hilo');after=pairs()
    assert sorted(before)==sorted(after)
    amounts=[Decimal(p[1:]) for n,p in after];assert amounts==sorted(amounts,reverse=True)
    return 'Ordre des prix décroissant ; tous les couples nom/prix conservés.'
def sort_names(ascending):
    login();select=Select(visible('product-sort-container'))
    if ascending: select.select_by_value('za')
    before=pairs();Select(visible('product-sort-container')).select_by_value('az' if ascending else 'za');after=pairs()
    assert sorted(before)==sorted(after)
    names=[n for n,p in after];assert names==sorted(names,reverse=not ascending)
    return f'Ordre des noms {"croissant" if ascending else "décroissant"} ; couples nom/prix conservés.'
def remove_last():
    login();add();click('remove-sauce-labs-backpack');visible('add-to-cart-sauce-labs-backpack')
    absent('shopping-cart-badge');cart();absent('inventory-item')
    return 'Dernier produit retiré ; bouton Add to cart restauré ; badge absent et panier vide.'
def continue_shopping():
    login();add();cart();click('continue-shopping');visible('inventory-list');cart();cart_one()
    return 'Continue Shopping ouvre le catalogue ; Backpack et badge 1 conservés au retour.'
def cancel_identity():
    login();add();cart();click('checkout');identity();click('cancel');visible('cart-list');cart_one();absent('complete-header')
    return 'Cancel depuis l’identité revient au panier ; Backpack conservé ; aucune confirmation.'
def cancel_overview():
    login();add();cart();click('checkout');identity();click('continue');visible('checkout-summary-container')
    click('cancel');visible('inventory-list');cart();cart_one();absent('complete-header')
    return 'Cancel depuis le récapitulatif revient au catalogue ; Backpack conservé ; aucune confirmation.'
def unauthorized():
    driver.get(BASE+'inventory.html');visible('login-button')
    assert 'You can only access' in visible('error').text;absent('inventory-list')
    return 'Accès direct anonyme refusé ; erreur de connexion visible ; aucun catalogue.'

checks=[('TC04',missing_username),('TC05',missing_password),('TC07',catalog_reference),('TC08',details),
        ('TC10',sort_prices_desc),('TC11',lambda:sort_names(True)),('TC12',lambda:sort_names(False)),
        ('TC16',remove_last),('TC18',continue_shopping),('TC20',cancel_identity),('TC23',cancel_overview),('TC24',unauthorized)]
for case_id,check in checks:
    start=datetime.now(timezone.utc)
    options=webdriver.ChromeOptions();options.add_argument('--headless=new');options.add_argument('--window-size=1440,1000')
    options.add_experimental_option('prefs',{'credentials_enable_service':False,'profile.password_manager_enabled':False,'profile.password_manager_leak_detection':False})
    driver=None;status='FAIL';observed='';error=''
    try:
        driver=webdriver.Chrome(options=options);driver.set_page_load_timeout(30);driver.set_window_size(1440,1000)
        driver.get(BASE)
        observed=check();status='PASS'
    except Exception:
        error=traceback.format_exc()
    finally:
        if driver:
            driver.save_screenshot(str(OUT/f'{case_id}.png'))
            caps=driver.capabilities
            browser=caps.get('browserVersion');driver_version=caps.get('chrome',{}).get('chromedriverVersion','').split(' ')[0]
            driver.quit()
        else: browser=driver_version='NOT STARTED'
    records.append(dict(case_id=case_id,status=status,method='Protocole ponctuel Selenium assisté, hors suite Robot',
                        start_utc=start.isoformat(),elapsed_seconds=round((datetime.now(timezone.utc)-start).total_seconds(),3),
                        observed=observed,error=error,browser_version=browser,driver_version=driver_version,screenshot=f'{case_id}.png'))
    (OUT/'results.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    print(case_id,status,observed or error.splitlines()[-1],flush=True)
with (OUT/'execution.csv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=records[0]);writer.writeheader();writer.writerows(records)
sys.exit(0 if all(r['status']=='PASS' for r in records) else 1)
