import json

all_css_rules = {
    '.zm-profile-header': {
        '.zm-profile-header-main': {
            '__use':'dump',
            'name':'.title-section .name::text',
            'sign':'.title-section .bio::text',
            'location':'.location.item::text',
            'business':'.business.item::text',
            'employment':'.employment.item::text',
            'position':'.position.item::text',
            'education':'.education.item::text',
            'education_extra':'.education-extra.item::text',
        }, '.zm-profile-header-operation': {
            '__use':'dump',
            'agree':'.zm-profile-header-user-agree strong::text',
            'thanks':'.zm-profile-header-user-thanks strong::text',
        }, '.profile-navbar': {
            '__use':'dump',
            'asks':'a[href*=asks] .num::text',
            'answers':'a[href*=answers] .num::text',
            'posts':'a[href*=posts] .num::text',
            'collections':'a[href*=collections] .num::text',
            'logs':'a[href*=logs] .num::text',
        },
    }, '.zm-profile-side-following': {
        '__use':'dump',
        'followees':'a.item[href*=followees] strong::text',
        'followers':'a.item[href*=followers] strong::text',
    }
}

def main():
	d1 = {'a':1, 'b':2}

	for k, v in d1.items():
		print k, v

	print all_css_rules
	json.dumps(all_css_rules, indent=4)

if __name__ == '__main__':
	main()