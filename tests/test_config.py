from tests import Base
from chinese.config import ConfigManager


class Config(Base):
    def test_get_fields(self):
        expected = ['English', '英文', '英語', '英语']
        self.assertEqual(ConfigManager().get_fields(['english']), expected)

    def test_get_fields_bad_group(self):
        self.assertEqual(ConfigManager().get_fields(['Foo']), [])

    def test_get_fields_no_arg(self):
        expected = [
            'Also Written',
            'Alternative',
            'Audio',
            'Bopomofo',
            'Cantonese',
            'Cantonese (Color)',
            'CantoSound',
            'Chinese',
            'Classifier',
            'ColorCant',
            'Color Cantonese',
            'Color Hanzi',
            'Color',
            'Color Traditional',
            'Deutsch',
            'English',
            "English Usage",
            "Examples",
            'Expression',
            'French',
            'Frequency',
            'German',
            'Hanzi (Color)',
            'Hanzi',
            'Measure Word',
            'Pinyin (Taiwan)',
            'Pinyin',
            'Reading',
            'Ruby (Bopomofo)',
            'Ruby (Cantonese)',
            'RubyCant',
            'Ruby (Pinyin)',
            'Ruby (Taiwan Pinyin)',
            'Ruby (Zhuyin)',
            'Ruby',
            'Silhouette',
            'Simp',
            'Simp.',
            'Simplified',
            'Sound (Cantonese)',
            'Sound (Mandarin)',
            'Sound',
            'Spoken',
            'Trad',
            'Trad.',
            'TradColor',
            'Traditional',
            'Traditional (Color)',
            "Usage",
            'Zhuyin',
            'le français',
            'ㄅㄆㄇㄈ',
            '中文',
            '台湾拼音',
            '台灣拼音',
            '声音',
            '大陆拼音',
            '大陸拼音',
            '广东话',
            '广州话',
            '廣州話',
            '廣東話',
            '彩色',
            '德文',
            '德語',
            '德语',
            '拼音',
            '汉字',
            '法文',
            '法語',
            '法语',
            '注音符号',
            '注音符號',
            '漢字',
            '简体',
            '简体字',
            '简化',
            '简化字',
            '簡化',
            '簡化字',
            '簡體',
            '簡體字',
            '粤',
            '粤拼',
            '粤语',
            '粵',
            '粵拼',
            '粵語',
            '繁体',
            '繁体字',
            '繁體',
            '繁體字',
            '聲音',
            '臺灣拼音',
            '英文',
            '英語',
            '英语',
            '註音符號',
            '量詞',
            '量词',
            'Simplified Classifier',
            'Simplified Measure Word',
            '繁体量詞',
            '简体量词',
            'Traditional Classifier',
            'Traditional Measure Word',
            '繁體量詞',
            '繁体量词',
            'Hanzi (Taiwan Color)',
            'Traditional (Taiwan Color)'
        ]
        self.assertCountEqual(ConfigManager().get_fields(), expected)
