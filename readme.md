# visualize_collatz_conjecture


##  dev环境
* install pyenv
  pyenv install 3.9.13
  pyenv shell 3.9.13

* 创建虚拟化环境
  
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
echo venv >> .gitignore

* 激活dev环境
source venv/bin/activate
python -m pip install --upgrade pip
* 安装所有依赖包
python -m pip install -r requirements.txt

## 依赖包

python -m pip install -U pytest
python -m pip freeze |grep pytest >> requirements.txt
python -m pip install -U pytest-html
python -m pip freeze |grep pytest-html >> requirements.txt

python -m pip install -U networkx
python -m pip freeze |grep networkx >> requirements.txt
python -m pip install -U matplotlib
python -m pip freeze |grep matplotlib >> requirements.txt
python -m pip install -U pygraphviz
python -m pip freeze |grep pygraphviz >> requirements.txt
python -m pip install -U pydot
python -m pip freeze |grep pydot >> requirements.txt
python -m pip install -U lxml
python -m pip freeze |grep lxml >> requirements.txt
python -m pip install -U scipy
python -m pip freeze |grep scipy >> requirements.txt


python -m pip install -U pyecharts
python -m pip freeze |grep pyecharts >> requirements.txt
seaborn
## setup autorun tasks
### npm : create package.json
### npm install npm-watch
echo node_modules >> .gitignore




