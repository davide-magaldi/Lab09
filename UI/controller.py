import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_anal(self, e):
        distance = self._view.txt_distance.value
        if distance is None or distance == "":
            self._view.create_alert("Inserire una distanza minima")
            return
        else:
            try:
                distance = int(distance)
            except ValueError:
                self._view.create_alert("Inserire un valore numerico!")
        self._model.buildGraph(distance)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumArchi()}"))
        for e in self._model.getEdges():
            self._view.txt_result.controls.append(ft.Text(f"{e[0].AIRPORT} - {e[1].AIRPORT} -- distanza media: {self._model._graph.get_edge_data(e[0], e[1])['weight']}"))
        self._view.update_page()
