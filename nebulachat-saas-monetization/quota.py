
import yaml

def check_quota(plan, tokens_used):
    with open('plans.yaml') as f:
        limits = yaml.safe_load(f)
    max_tokens = limits[plan]['max_tokens']
    return tokens_used <= max_tokens
