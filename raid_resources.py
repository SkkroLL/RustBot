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

    #ресурсы для крафта c4
    c4_explosives = explosives * quantity
    c4_tech_trash = tech_trash * quantity
    c4_cloth = cloth * quantity

    #ресурсы для крафта взрывчатого вещества
    explosives_powder = Explosives['gun_powder'] * explosives * quantity
    explosives_fuel = Explosives['fuel'] * explosives * quantity
    explosives_sulfur = Explosives['sulfur'] * explosives * quantity
    explosives_metal = Explosives['metal'] * explosives * quantity

    # ресурсы для крафта пороха
    powder_sulfur = (gun_powder['sulfur'] * explosives_powder)/10
    powder_charcoal = (gun_powder['charcoal'] * explosives_powder)/10

    full_c4 = {
        'взрывчатое вещество': c4_explosives,
        'Ткань': c4_cloth,
        'старые микросхемы': c4_tech_trash,
        'Порох': explosives_powder,
        'Топливо': explosives_fuel,
        'Сера для ВВ': explosives_sulfur,
        'Металл': explosives_metal,
        'Уголь': powder_charcoal,
        'Сера для пороха': powder_sulfur
    }
    return full_c4

def rocket(quantity):
    """Количество ресурсов для крафта ракет"""
    metal_pipe = 2
    explosives = 10
    powder = 150

    #ресурсы для крафта ракет
    rocket_explosives = explosives * quantity
    rocket_metal_pipe = metal_pipe * quantity
    rocket_powder = powder * quantity

    #ресурсы для крафта взрывчатого вещества
    explosives_powder = Explosives['gun_powder'] * explosives * quantity
    explosives_fuel = Explosives['fuel'] * explosives * quantity
    explosives_sulfur = Explosives['sulfur'] * explosives * quantity
    explosives_metal = Explosives['metal'] * explosives * quantity

    #ресурсы для крафта пороха
    powder_sulfur = ((gun_powder['sulfur'] * explosives_powder) + (gun_powder['sulfur'] * rocket_powder))/10
    powder_charcoal = ((gun_powder['charcoal'] * explosives_powder) + (gun_powder['charcoal'] * rocket_powder))/10

    full_rocket = {
        'взрывчатое вещество': rocket_explosives,
        'Металлические трубы': rocket_metal_pipe,
        'Порох для ракет': rocket_powder,
        'Порох для ВВ': explosives_powder,
        'Топливо': explosives_fuel,
        'Сера для ВВ': explosives_sulfur,
        'Металл': explosives_metal,
        'Уголь': powder_charcoal,
        'Сера для пороха': powder_sulfur,
    }
    return full_rocket

def beancan_grenade(quantity):
    """Количество ресурсов для крафта бобовых гранат"""
    metal = 20
    powder = 60

    #ресурсы для крафта бобовых гранат
    grenade_powder = powder * quantity
    grenade_metal = metal * quantity

    #ресурсы для крафта пороха
    powder_sulfur = (gun_powder['sulfur'] * grenade_powder)/10
    powder_charcoal = (gun_powder['charcoal'] * grenade_powder)/10

    full_beancan_grenade = {
        'Металл': grenade_metal,
        'Порох': grenade_powder,
        'Сера': powder_sulfur,
        'Уголь': powder_charcoal,
    }
    return full_beancan_grenade

def satchels(quantity):
    """Количество ресурсов для крафта сачелей"""
    rope = 1
    small_stash = 1
    grenades = 4

    #ресурсы для крафта сачелей
    satchels_grenades = grenades * quantity
    satchels_small_stash = small_stash * quantity
    satchels_rope = rope * quantity

    #ресурсы для крафта бобовых гранат
    resources_for_grenades = beancan_grenade(satchels_grenades)
    grenade_powder = resources_for_grenades['Порох']
    grenade_metal = resources_for_grenades['Металл']

    #ресурсы для крафта пороха
    powder_sulfur = resources_for_grenades['Сера']
    powder_charcoal = resources_for_grenades['Уголь']

    full_satchels = {
        'Бобовая граната': satchels_grenades,
        'Маленький тайник': satchels_small_stash,
        'Веревка': satchels_rope,
        'порох': grenade_powder,
        'Металл': grenade_metal,
        'Сера': powder_sulfur,
        'Уголь': powder_charcoal,
    }
    return full_satchels

def explosive_ammos(quantity):
    """Количество ресурсов для крафта разрывных патронов"""
    metal = 10
    powder = 10
    sulfur = 10

    #ресурсы для крафта патронов
    ammos_metal = metal * quantity
    ammos_powder = powder * quantity
    ammos_sulfur = sulfur * quantity

    #ресурсы для крафта пороха
    powder_charcoal = (gun_powder['charcoal'] * ammos_powder)/10
    powder_sulfur = (gun_powder['sulfur'] * ammos_sulfur)/10

    full_explosive_ammos = {
        'Порох': ammos_powder,
        'Металл': ammos_metal,
        'Сера для патронов': ammos_sulfur,
        'Уголь': powder_charcoal,
        'Сера для пороха': powder_sulfur
    }
    return full_explosive_ammos

