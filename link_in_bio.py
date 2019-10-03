from flask import Flask, render_template
import yaml

app = Flask(__name__)


def open_master(filename='info.yml'):
    with open(filename, mode='r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f'{exc} error on opening yml')


master_unfiltered = open_master()
master = {}
for key, values in master_unfiltered.items():
    if 'links' in key:
        for link_dicts in values:
            for inner_dict in link_dicts.items():
                temporary = []
                if 'facebook' in inner_dict[0]:
                    fbdict = inner_dict[1]
                    master.update({inner_dict[0]: inner_dict[1]})
                elif 'twitter' in inner_dict[0]:
                    twdict = inner_dict[1]
                    master.update({inner_dict[0]: inner_dict[1]})
                elif 'instagram' in inner_dict[0]:
                    igdict = inner_dict[1]
                    master.update({inner_dict[0]: inner_dict[1]})
                elif 'linkedin' in inner_dict[0]:
                    lidict = inner_dict[1]
                    master.update({inner_dict[0]: inner_dict[1]})


@app.route("/")
def main_page():
    pass


# if __name__ == "__main__":
#     app.run()
