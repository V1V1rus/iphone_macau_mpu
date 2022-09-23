# 库存地址
import json

url = "https://reserve-prime.apple.com/MO/zh_MO/reserve/A/availability.json"

# 店铺
stores = {
    'R672': '澳門銀河',
    'R697': '路氹金光大道',
}

# 浏览器头
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
}

# 钉钉机器人
dingtalk = 'https://oapi.dingtalk.com/robot/send?access_token=803376f467404d88613e0f60eb9c1594a7a110b84fffc8f55534e4dd7c38c3c9'
secret = 'SECbd03f36b08313bb3127def4f6e083771050b475fde7d2bb2a8ce348abe39616d'

# 手机型号
iPhones = {
    # 'MQ2R3ZA/A': 'iPhone 14 Pro 1TB 金色',
    # 'MPXR3ZA/A': 'iPhone 14 Pro 128GB 太空黑',
    'MQ873ZA/A': 'iPhone 14 Pro Max 256GB 太空黑',
    # 'MQ1C3ZA/A': 'iPhone 14 Pro 256GB 暗紫色',
    # 'MQ8L3ZA/A': 'iPhone 14 Pro Max 1TB 金色',
    # 'MQ143ZA/A': 'iPhone 14 Pro 256GB 金色',
    # 'MQ203ZA/A': 'iPhone 14 Pro 512GB 金色',
    # 'MQ263ZA/A': 'iPhone 14 Pro 512GB 暗紫色',
    # 'MQ053ZA/A': 'iPhone 14 Pro 128GB 金色',
    # 'MQ863ZA/A': 'iPhone 14 Pro Max 128GB 暗紫色',
    # 'MQ2K3ZA/A': 'iPhone 14 Pro 1TB 銀色',
    # 'MQ0D3ZA/A': 'iPhone 14 Pro 128GB 暗紫色',
    'MQ8A3ZA/A': 'iPhone 14 Pro Max 256GB 暗紫色',
    # 'MQ893ZA/A': 'iPhone 14 Pro Max 256GB 金色',
    # 'MQ843ZA/A': 'iPhone 14 Pro Max 128GB 銀色',
    # 'MQ8F3ZA/A': 'iPhone 14 Pro Max 512GB 金色',
    # 'MQ2D3ZA/A': 'iPhone 14 Pro 1TB 太空黑',
    # 'MQ8H3ZA/A': 'iPhone 14 Pro Max 1TB 太空黑',
    # 'MQ8D3ZA/A': 'iPhone 14 Pro Max 512GB 太空黑',
    # 'MQ2Y3ZA/A': 'iPhone 14 Pro 1TB 暗紫色',
    # 'MQ1J3ZA/A': 'iPhone 14 Pro 512GB 太空黑',
    # 'MQ8M3ZA/A': 'iPhone 14 Pro Max 1TB 暗紫色',
    # 'MQ833ZA/A': 'iPhone 14 Pro Max 128GB 太空黑',
    # 'MQ8J3ZA/A': 'iPhone 14 Pro Max 1TB 銀色',
    # 'MPXY3ZA/A': 'iPhone 14 Pro 128GB 銀色',
    # 'MQ8G3ZA/A': 'iPhone 14 Pro Max 512GB 暗紫色',
    # 'MQ8E3ZA/A': 'iPhone 14 Pro Max 512GB 銀色',
    'MQ883ZA/A': 'iPhone 14 Pro Max 256GB 銀色',
    # 'MQ1R3ZA/A': 'iPhone 14 Pro 512GB 銀色',
    # 'MQ853ZA/A': 'iPhone 14 Pro Max 128GB 金色',
    # 'MQ0M3ZA/A': 'iPhone 14 Pro 256GB 太空黑',
    # 'MQ0W3ZA/A': 'iPhone 14 Pro 256GB 銀色'
}

subfamily = {
    # 'MQ2R3ZA/A': 'iPhone 14 Pro 1TB 金色',
    # 'MPXR3ZA/A': 'iPhone 14 Pro 128GB 太空黑',
    'MQ873ZA/A': 'iPhone 14 Pro Max',
    # 'MQ1C3ZA/A': 'iPhone 14 Pro 256GB 暗紫色',
    # 'MQ8L3ZA/A': 'iPhone 14 Pro Max 1TB 金色',
    # 'MQ143ZA/A': 'iPhone 14 Pro 256GB 金色',
    # 'MQ203ZA/A': 'iPhone 14 Pro 512GB 金色',
    # 'MQ263ZA/A': 'iPhone 14 Pro 512GB 暗紫色',
    # 'MQ053ZA/A': 'iPhone 14 Pro 128GB 金色',
    # 'MQ863ZA/A': 'iPhone 14 Pro Max 128GB 暗紫色',
    # 'MQ2K3ZA/A': 'iPhone 14 Pro 1TB 銀色',
    'MQ0D3ZA/A': 'iPhone 14 Pro',
    'MQ8A3ZA/A': 'iPhone 14 Pro Max',
    # 'MQ893ZA/A': 'iPhone 14 Pro Max 256GB 金色',
    # 'MQ843ZA/A': 'iPhone 14 Pro Max 128GB 銀色',
    # 'MQ8F3ZA/A': 'iPhone 14 Pro Max 512GB 金色',
    # 'MQ2D3ZA/A': 'iPhone 14 Pro 1TB 太空黑',
    # 'MQ8H3ZA/A': 'iPhone 14 Pro Max 1TB 太空黑',
    # 'MQ8D3ZA/A': 'iPhone 14 Pro Max 512GB 太空黑',
    # 'MQ2Y3ZA/A': 'iPhone 14 Pro 1TB 暗紫色',
    # 'MQ1J3ZA/A': 'iPhone 14 Pro 512GB 太空黑',
    # 'MQ8M3ZA/A': 'iPhone 14 Pro Max 1TB 暗紫色',
    # 'MQ833ZA/A': 'iPhone 14 Pro Max 128GB 太空黑',
    # 'MQ8J3ZA/A': 'iPhone 14 Pro Max 1TB 銀色',
    # 'MPXY3ZA/A': 'iPhone 14 Pro 128GB 銀色',
    # 'MQ8G3ZA/A': 'iPhone 14 Pro Max 512GB 暗紫色',
    # 'MQ8E3ZA/A': 'iPhone 14 Pro Max 512GB 銀色',
    'MQ883ZA/A': 'iPhone 14 Pro Max',
    # 'MQ1R3ZA/A': 'iPhone 14 Pro 512GB 銀色',
    # 'MQ853ZA/A': 'iPhone 14 Pro Max 128GB 金色',
    # 'MQ0M3ZA/A': 'iPhone 14 Pro 256GB 太空黑',
    # 'MQ0W3ZA/A': 'iPhone 14 Pro 256GB 銀色'
}

colors = {
    # 'MQ2R3ZA/A': 'iPhone 14 Pro 1TB 金色',
    # 'MPXR3ZA/A': 'iPhone 14 Pro 128GB 太空黑',
    'MQ873ZA/A': '太空黑',
    # 'MQ1C3ZA/A': 'iPhone 14 Pro 256GB 暗紫色',
    # 'MQ8L3ZA/A': 'iPhone 14 Pro Max 1TB 金色',
    # 'MQ143ZA/A': 'iPhone 14 Pro 256GB 金色',
    # 'MQ203ZA/A': 'iPhone 14 Pro 512GB 金色',
    # 'MQ263ZA/A': 'iPhone 14 Pro 512GB 暗紫色',
    # 'MQ053ZA/A': 'iPhone 14 Pro 128GB 金色',
    # 'MQ863ZA/A': 'iPhone 14 Pro Max 128GB 暗紫色',
    # 'MQ2K3ZA/A': 'iPhone 14 Pro 1TB 銀色',
    'MQ0D3ZA/A': '暗紫色',
    'MQ8A3ZA/A': '暗紫色',
    # 'MQ893ZA/A': 'iPhone 14 Pro Max 256GB 金色',
    # 'MQ843ZA/A': 'iPhone 14 Pro Max 128GB 銀色',
    # 'MQ8F3ZA/A': 'iPhone 14 Pro Max 512GB 金色',
    # 'MQ2D3ZA/A': 'iPhone 14 Pro 1TB 太空黑',
    # 'MQ8H3ZA/A': 'iPhone 14 Pro Max 1TB 太空黑',
    # 'MQ8D3ZA/A': 'iPhone 14 Pro Max 512GB 太空黑',
    # 'MQ2Y3ZA/A': 'iPhone 14 Pro 1TB 暗紫色',
    # 'MQ1J3ZA/A': 'iPhone 14 Pro 512GB 太空黑',
    # 'MQ8M3ZA/A': 'iPhone 14 Pro Max 1TB 暗紫色',
    # 'MQ833ZA/A': 'iPhone 14 Pro Max 128GB 太空黑',
    # 'MQ8J3ZA/A': 'iPhone 14 Pro Max 1TB 銀色',
    # 'MPXY3ZA/A': 'iPhone 14 Pro 128GB 銀色',
    # 'MQ8G3ZA/A': 'iPhone 14 Pro Max 512GB 暗紫色',
    # 'MQ8E3ZA/A': 'iPhone 14 Pro Max 512GB 銀色',
    'MQ883ZA/A': '銀色',
    # 'MQ1R3ZA/A': 'iPhone 14 Pro 512GB 銀色',
    # 'MQ853ZA/A': 'iPhone 14 Pro Max 128GB 金色',
    # 'MQ0M3ZA/A': 'iPhone 14 Pro 256GB 太空黑',
    # 'MQ0W3ZA/A': 'iPhone 14 Pro 256GB 銀色'
}

capacity = {
    # 'MQ2R3ZA/A': 'iPhone 14 Pro 1TB 金色',
    # 'MPXR3ZA/A': 'iPhone 14 Pro 128GB 太空黑',
    'MQ873ZA/A': '256GB',
    # 'MQ1C3ZA/A': 'iPhone 14 Pro 256GB 暗紫色',
    # 'MQ8L3ZA/A': 'iPhone 14 Pro Max 1TB 金色',
    # 'MQ143ZA/A': 'iPhone 14 Pro 256GB 金色',
    # 'MQ203ZA/A': 'iPhone 14 Pro 512GB 金色',
    # 'MQ263ZA/A': 'iPhone 14 Pro 512GB 暗紫色',
    # 'MQ053ZA/A': 'iPhone 14 Pro 128GB 金色',
    # 'MQ863ZA/A': 'iPhone 14 Pro Max 128GB 暗紫色',
    # 'MQ2K3ZA/A': 'iPhone 14 Pro 1TB 銀色',
    'MQ0D3ZA/A': '128GB',
    'MQ8A3ZA/A': '256GB',
    # 'MQ893ZA/A': 'iPhone 14 Pro Max 256GB 金色',
    # 'MQ843ZA/A': 'iPhone 14 Pro Max 128GB 銀色',
    # 'MQ8F3ZA/A': 'iPhone 14 Pro Max 512GB 金色',
    # 'MQ2D3ZA/A': 'iPhone 14 Pro 1TB 太空黑',
    # 'MQ8H3ZA/A': 'iPhone 14 Pro Max 1TB 太空黑',
    # 'MQ8D3ZA/A': 'iPhone 14 Pro Max 512GB 太空黑',
    # 'MQ2Y3ZA/A': 'iPhone 14 Pro 1TB 暗紫色',
    # 'MQ1J3ZA/A': 'iPhone 14 Pro 512GB 太空黑',
    # 'MQ8M3ZA/A': 'iPhone 14 Pro Max 1TB 暗紫色',
    # 'MQ833ZA/A': 'iPhone 14 Pro Max 128GB 太空黑',
    # 'MQ8J3ZA/A': 'iPhone 14 Pro Max 1TB 銀色',
    # 'MPXY3ZA/A': 'iPhone 14 Pro 128GB 銀色',
    # 'MQ8G3ZA/A': 'iPhone 14 Pro Max 512GB 暗紫色',
    # 'MQ8E3ZA/A': 'iPhone 14 Pro Max 512GB 銀色',
    'MQ883ZA/A': '256GB',
    # 'MQ1R3ZA/A': 'iPhone 14 Pro 512GB 銀色',
    # 'MQ853ZA/A': 'iPhone 14 Pro Max 128GB 金色',
    # 'MQ0M3ZA/A': 'iPhone 14 Pro 256GB 太空黑',
    # 'MQ0W3ZA/A': 'iPhone 14 Pro 256GB 銀色'
}