# Ресурсы для крафта взрывчатого вещества
Explosives = {
    'gun_powder': 50,
    'fuel': 3,
    'sulfur': 10,
    'metal': 10
}
#Количество ресурсов для крафта пороха
gun_powder = {
    'charcoal': 30,
    'sulfur': 20
}

def c4(quantity):
    """Количество ресурсов для крафта C4"""
    explosives = 20
    cloth = 5
    tech_trash = 2

    full_explosives = explosives * quantity
    full_tech_trash = tech_trash * quantity
    full_cloth = cloth * quantity
    full_powder = Explosives['gun_powder'] * explosives * quantity
    full_fuel = Explosives['fuel'] * explosives * quantity
    full_sulfur = Explosives['sulfur'] * explosives * quantity + (gun_powder['sulfur']*full_powder)/10
    full_metal = Explosives['metal'] * explosives * quantity
    full_charcoal = (gun_powder['charcoal'] * full_powder)/10

    full_c4 = {
        'взрывчатое вещество': full_explosives,
        'Ткань': full_cloth,
        'старые микросхемы': full_tech_trash,
        'Порох': full_powder,
        'Топливо': full_fuel,
        'Сера': full_sulfur,
        'Металл': full_metal,
        'Уголь': full_charcoal
    }
    return full_c4

def rocket(quantity):
    """Количество ресурсов для крафта ракет"""
    metal_pipe = 2
    explosives = 10
    powder = 150

    full_explosives = explosives * quantity
    full_metal_pipe = metal_pipe * quantity
    full_powder = Explosives['gun_powder'] * explosives * quantity + (powder * quantity)
    full_fuel = Explosives['fuel'] * explosives * quantity
    full_sulfur = Explosives['sulfur'] * explosives * quantity + (gun_powder['sulfur']*full_powder)/10
    full_metal = Explosives['metal'] * explosives * quantity
    full_charcoal = (gun_powder['charcoal'] * full_powder) / 10

    full_rocket = {
        'взрывчатое вещество': full_explosives,
        'Порох': full_powder,
        'Топливо': full_fuel,
        'Сера': full_sulfur,
        'Металл': full_metal,
        'Уголь': full_charcoal,
        'Металлические трубы': full_metal_pipe,
    }
    return full_rocket

def beancan_grenade(quantity):
    """Количество ресурсов для крафта бобовых гранат"""
    metal = 20
    powder = 60

    full_powder = powder * quantity
    full_sulfur = (gun_powder['sulfur'] * full_powder) / 10
    full_charcoal = (gun_powder['charcoal'] * full_powder) / 10
    full_metal = metal * quantity

    full_beancan_grenade = {
        'Порох': full_powder,
        'Сера': full_sulfur,
        'Уголь': full_charcoal,
        'Металл': full_metal
    }
    return full_beancan_grenade

def satchels(quantity):
    """Количество ресурсов для крафта сачелей"""
    rope = 1
    small_stash = 1
    grenades = 4

    full_grenades = grenades * quantity
    full_small_stash = small_stash * quantity
    full_rope = rope * quantity
    resources_for_grenades = beancan_grenade(full_grenades)

    full_satchels = {
        'Веревка': full_rope,
        'Маленький тайник': full_small_stash,
        'Бобовая граната': full_grenades,
        'порох': resources_for_grenades['Порох'],
        'Сера': resources_for_grenades['Сера'],
        'Уголь': resources_for_grenades['Уголь'],
        'Металл': resources_for_grenades['Металл'],
    }
    return full_satchels

def explosive_ammos(quantity):
    """Количество ресурсов для крафта разрывных патронов"""
    metal = 10
    powder = 10
    sulfur = 10

    full_metal = metal * quantity
    full_powder = powder * quantity
    full_sulfur = sulfur * quantity + (gun_powder['sulfur'] * full_powder)/10
    full_charcoal = (gun_powder['charcoal'] * full_powder)/10

    full_explosive_ammos = {
        'Порох': full_powder,
        'Металл': full_metal,
        'Сера': full_sulfur,
        'Уголь': full_charcoal
    }
    return full_explosive_ammos

print(explosive_ammos(2))
