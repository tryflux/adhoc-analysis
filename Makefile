
folder=$(CURDIR)

install-jupyter-plotly:
	jupyter labextension install jupyterlab-plotly@4.14.3 @jupyter-widgets/jupyterlab-manager plotlywidget@4.14.3

jupyter:
	PYTHONPATH=${folder}/src PROJECTROOT=${folder} jupyter lab
