import pandas as pd2

categories_diesel: dict[str: str] = {
    "11201": 'Буровые станки "ROC"',
    "11203": 'Буровые станки "ROC"',
    "11211": 'Буровые станки "ROC"',
    "11204": 'Буровые станки "ROC"',
    "11205": 'Буровые станки "ROC"',
    "11209": 'Буровые станки "ROC"',
    "11210": 'Буровые станки "ROC"',
    "11301": "Погрузчики",
    "11302": "Погрузчики",
    "11303": "Погрузчики",
    "11304": "Погрузчики",
    "11305": "Погрузчики",
    "11306": "Погрузчики",
    "11307": "Погрузчики",
    "11308": "Погрузчики",
    "11310": "Погрузчики",
    "11311": "Погрузчики",
    "11313": "Погрузчики",
    "11404": "Экскаваторы",
    "11405": "Экскаваторы",
    "11406": "Экскаваторы",
    "11407": "Экскаваторы",
    "11408": "Экскаваторы",
    "11409": "Экскаваторы",
    "11410": "Экскаваторы",
    "11411": "Экскаваторы",
    "11501": "Бульдозеры",
    "11504": "Бульдозеры",
    "11505": "Бульдозеры",
    "11507": "Бульдозеры",
    "11508": "Бульдозеры",
    "11509": "Бульдозеры",
    "11510": "Бульдозеры",
    "11511": "Бульдозеры",
    "11512": "Бульдозеры",
    "11513": "Бульдозеры",
    "11514": "Бульдозеры",
    "11522": "Бульдозеры",
    "11517": "Бульдозеры",
    "11603": 'Самосвалы "Caterpillar"',
    "11605": 'Самосвалы "Caterpillar"',
    "11607": 'Самосвалы "Caterpillar"',
    "11608": 'Самосвалы "Caterpillar"',
    "11609": 'Самосвалы "БЕЛАЗ"',
    "11610": 'Самосвалы "БЕЛАЗ"',
    "11612": 'Самосвалы "БЕЛАЗ"',
    "11613": 'Самосвалы "БЕЛАЗ"',
    "11614": 'Самосвалы "БЕЛАЗ"',
    "11616": 'Самосвалы "БЕЛАЗ"',
    "11618": 'Самосвалы "БЕЛАЗ"',
    "11619": 'Самосвалы "БЕЛАЗ"',
    "11620": 'Самосвалы "БЕЛАЗ"',
    "11621": 'Самосвалы "БЕЛАЗ"',
    "11622": 'Самосвалы "LGMG"',
    "11623": 'Самосвалы "LGMG"',
    "11624": 'Самосвалы "LGMG"',
    "11625": 'Самосвалы "LGMG"',
    "11632": 'Самосвалы "LGMG"',
    "11633": 'Самосвалы "LGMG"',
    "11634": 'Самосвалы "LGMG"',
    "11635": 'Самосвалы "LGMG"',
    "11626": 'Самосвалы "Komatsu"',
    "11627": 'Самосвалы "Komatsu"',
    "11628": 'Самосвалы "Komatsu"',
    "11629": 'Самосвалы "Komatsu"',
    "11630": 'Самосвалы "Komatsu"',
    "11631": 'Самосвалы "Komatsu"',
    "11713": 'Самосвалы "КАМАЗ" "Shacman"',
    "11719": 'Самосвалы "КАМАЗ" "Shacman"',
    "11721": 'Самосвалы "КАМАЗ" "Shacman"',
    "11725": 'Самосвалы "КАМАЗ" "Shacman"',
    "11726": 'Самосвалы "КАМАЗ" "Shacman"',
    "11727": 'Самосвалы "КАМАЗ" "Shacman"',
    "11636": 'Самосвалы "КАМАЗ" "Shacman"',
    "11637": 'Самосвалы "КАМАЗ" "Shacman"',
    "11638": 'Самосвалы "КАМАЗ" "Shacman"',
    "12101": 'ПГР - Буровые установки BOOMER, Boltec, Simba',
    "12102": 'ПГР - Буровые установки BOOMER, Boltec, Simba',
    "12103": 'ПГР - Буровые установки BOOMER, Boltec, Simba',
    "12104": 'ПГР - Буровые установки BOOMER, Boltec, Simba',
    "12106": 'ПГР - Буровые установки BOOMER, Boltec, Simba',
    "12107": 'ПГР - Буровые установки BOOMER, Boltec, Simba',
    "12201": 'ПГР - Шахтные погрузчики',
    "12202": 'ПГР - Шахтные погрузчики',
    "12203": 'ПГР - Шахтные погрузчики',
    "12204": 'ПГР - Шахтные погрузчики',
    "12205": 'ПГР - Шахтные погрузчики',
    "12206": 'ПГР - Шахтные погрузчики',
    "12207": 'ПГР - Шахтные погрузчики',
    "12208": 'ПГР - Шахтные погрузчики',
    "12209": 'ПГР - Шахтные погрузчики',
    "12210": 'ПГР - Шахтные погрузчики',
    "12211": 'ПГР - Шахтные погрузчики',
    "12301": 'ПГР - Шахтные самосвалы',
    "12302": 'ПГР - Шахтные самосвалы',
    "12303": 'ПГР - Шахтные самосвалы',
    "12304": 'ПГР - Шахтные самосвалы',
    "12305": 'ПГР - Шахтные самосвалы',
    "12306": 'ПГР - Шахтные самосвалы',
    "12401": 'ПГР - Вспомогательная машина "Multimec"',
    "12403": 'ПГР - Вспомогательная машина "Multimec"',
    "12402": 'ПГР - Зарядная машина Charmec',
    "12407": 'ПГР - Зарядная машина Charmec',
    "12408": 'ПГР - Зарядная машина Charmec',
    "13102": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13103": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13104": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13105": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13201": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13203": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13207": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13300": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13407": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13401": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13402": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13403": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13404": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13501": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13502": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13503": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13504": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13505": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13507": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13508": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13510": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13511": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13512": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13514": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13515": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13523": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13530": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13602": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13616": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13622": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13604": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13701": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13703": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13707": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13708": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13706": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13526": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13539": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13540": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13541": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13542": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13543": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13544": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13561": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13562": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13563": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13524": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13525": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13529": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13532": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13533": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13534": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13535": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13536": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13545": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13546": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13547": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13548": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13549": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13550": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13551": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13552": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13553": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13554": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13555": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13556": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13557": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13558": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13559": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13566": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "472820": 'Обслуживающая техника (вахтовки, парм, подъёмники, краны и др.)',
    "13808": 'Легковые машины',
    "13817": 'Легковые машины',
    "13816": 'Легковые машины',
    "13823": 'Легковые машины',
    "13804": 'Легковые машины',
    "13821": 'Легковые машины',
    "13807": 'Легковые машины',
    "13806": 'Легковые машины',
    "14419": 'Дробилка METSO LOKOTRAK',
    "16401": 'Насосы Godwin',
    "16402": 'Насосы Godwin',
    "16405": 'Насосы Godwin',
    "16406": 'Насосы Godwin',
    "17702": 'Комплекс Kiturami',
    "17302": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17303": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17304": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17305": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17307": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17308": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17310": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17311": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17312": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17313": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17314": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17315": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17316": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17317": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17318": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17503": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17401": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17402": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17403": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17404": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17405": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17406": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17407": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17408": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17409": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17411": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17412": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17413": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17414": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17415": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17416": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17417": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17418": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17419": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17420": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17421": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17422": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "17423": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "13824": 'Передвижные и прочие ДЭС "Энергопрогноз", ГАЗ СобольX96231073N2868687',
    "13818": "Подрядные организации",
    "13565": "Подрядные организации",
    "13537": "Подрядные организации",
    "13831": "Подрядные организации",
    "Буровая установка СБУ-5ГПРМ HDR-5S": "Подрядные организации",
    "Бульдозер Shantui SD32 20001": "Подрядные организации",
    "40001 Бульдозер ZoomLion SD22": "Подрядные организации",
    "40001": "Подрядные организации",
    "Урал NexT 4320 884(вода)": "Подрядные организации",
    "Урал NexT 4320 884": "Подрядные организации",
    "Урал NexT 4320 280(ПРМ)": "Подрядные организации",
    "Урал NexT 4320 280": "Подрядные организации",
    "Урал NexT 4320 182(вахта)": "Подрядные организации",
    "Урал NexT 4320 182": "Подрядные организации",
    'Участок ПГР Аметистовое': "Подотчёт - участок ПГР",
    'Склад ВМ': "Склад ВМ - Производство ВВ",
    'Емкость РММ Аметистовое': "Подотчёт - Подразделения",
    'склад ТМЦ  АО "Аметистовое"': "Подотчёт - Подразделения",
    '0103М0020_Рудник/участок ГРР/ЭРБ': "Подотчёт - Подразделения",
    'Начальник АТЦ': "Подотчёт - участок АТЦ",
    'Рудник/участок БВР/ОГР': "Подотчёт - Подразделения",
    'Комплекс ПК № 39': "Комплекс ПК № 39",
    'Комплекс ДЭС №24': 'АТЭС "Энергопрогноз"',
    'АТЭС': 'АТЭС "Энергопрогноз"'

}

categories_petrol = {
    "12406": "12406 Автомобиль УАЗ Фермер(ПГР)",
    "13815": "13815 Автомобиль UAZ PICKUP - ХТТ236320L1016082",
    "13803": "13803 Автомобиль УАЗ - 23632 VIN ХТТ236320Н1007480 гос № В546ВХ",
    "13801": "13801 Автомобиль УАЗ - 23632 VIN ХТТ236320Н1006120 гос. № В639ВХ",
    "13814": "13814 Автомобиль UAZ PICKUP - ХТТ236320L1016081",
    "13828": "13828 УАЗ Хантер XTT292400P1000002 Белый",
    "13825": "13825 УАЗ Фермер ГРР VIN:ХТТ390945N1213193",
    "13827": "13827 УАЗ Пикап XTT236320P1008253 Серебристый",
    "13826": "13826 УАЗ Пикап XTT236320P1007995 Темно-серый",
    "12405": "12405 Автомобиль UAZ HUNTER(СГМарк)",
    "13811": "13811 Мотовездеход POLARIS SPORTSMAN 800 EFI 6*6 гос№ 22-56КА",
    "13832": "13832 УАЗ Пикап ХТТ236320R1008525",
    "13833": "13833 УАЗ Фермер Эл.Мех. VIN:ХТТ390945R1205639",
    "some": "Бензин подрядные организации (РБК, ВиЭй Сервис)",
    "other": "Бензин - прочие нужды"
}



