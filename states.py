from aiogram.dispatcher.filters.state import State,StatesGroup

class about_company(StatesGroup):
    about_company=State()
    about_partners=State()
    about_workers=State()
    about_clients=State()
    about_certifications=State()
    contact_us=State()
    location_us=State()
    count=State()

class btns(StatesGroup):
    next=State()
    prev=State()