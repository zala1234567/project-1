from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button


# Función de validación para entrada de números positivos y decimales
def validar_entrada(instance, value):
    # Permite solo dígitos y el punto decimal, no permite el ingreso de '-' para números negativos
    if value.isdigit() or value == "" or (value.count('.') == 1 and value[0] != '.'):
        return True
    else:
        return False

# Función para calcular y mostrar resultados
def calcular(instance):
    try:
        inv = float(entrada_inv.text)
        pori = float(entrada_pori.text)
        num_resultados = min(int(entrada_num_resultados.text), 20)  # Límite ajustado a 20 resultados

        asc_texto_resultados = "Ascendente:\n"  # Cambiado el identificador
        des_texto_resultados = "Descendente:\n"  # Cambiado el identificador
        
        por_asc = 1 + (pori / 100)
        por_des = 1 - (pori / 100)
        tot_asc = inv
        tot_des = inv
        for x in range(1, num_resultados + 1):
            tot_asc *= por_asc
            tot_des *= por_des
            asc_texto_resultados += f"{x}: {tot_asc:.2f}$\n"  # Modificado el formato del resultado
            des_texto_resultados += f"{x}: {tot_des:.2f}$\n"  # Modificado el formato del resultado
            
        resultados_asc.text = asc_texto_resultados
        resultados_des.text = des_texto_resultados
            
    except ValueError:
        resultados_asc.text = "Por favor, ingrese valores válidos."
        resultados_des.text = "Por favor, ingrese valores válidos."

class MyKivyApp(App):
    def build(self):
        layout = FloatLayout()

        # Crear un BoxLayout para agrupar las casillas de entrada con un pequeño espaciado
        input_group = BoxLayout(orientation='vertical', size_hint=(1, None), height=150, pos_hint={'center_x': 0.5, 'top': 0.95}, spacing=5)

        # Variables de entrada
        global entrada_inv, entrada_pori, entrada_num_resultados
        entrada_inv = TextInput(hint_text="Inversión inicial", input_filter='float', multiline=False, size_hint=(1, None), height=40)
        entrada_pori = TextInput(hint_text="Porcentaje", input_filter='float', multiline=False, size_hint=(1, None), height=40)
        entrada_num_resultados = TextInput(hint_text="Número de resultados (20 max)", input_filter='int', multiline=False, size_hint=(1, None), height=40)
        calcular_button = Button(text="Calcular", size_hint=(1, None), height=40)

        # Registro de la función de validación
        entrada_inv.bind(text=validar_entrada)
        entrada_pori.bind(text=validar_entrada)
        entrada_num_resultados.bind(text=validar_entrada)

        # Evento de clic para el botón de cálculo
        calcular_button.bind(on_press=calcular)

        # Añadir widgets al grupo de entrada
        input_group.add_widget(entrada_inv)
        input_group.add_widget(entrada_pori)
        input_group.add_widget(entrada_num_resultados)
        input_group.add_widget(calcular_button)

        # Resultados
        global resultados_asc, resultados_des
        resultados_asc = TextInput(text="", readonly=True, multiline=True, background_color=(0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1))
        resultados_des = TextInput(text="", readonly=True, multiline=True, background_color=(0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1))


        # Crear un ScrollView para los resultados
        scroll_view_asc = ScrollView(size_hint=(0.5, 0.5), pos_hint={'center_x': 0.25, 'y': 0.3})
        scroll_view_des = ScrollView(size_hint=(0.5, 0.5), pos_hint={'center_x': 0.75, 'y': 0.3})
        scroll_view_asc.add_widget(resultados_asc)
        scroll_view_des.add_widget(resultados_des)

        layout.add_widget(input_group)
        layout.add_widget(scroll_view_asc)
        layout.add_widget(scroll_view_des)

        return layout

if __name__ == "__main__":
    MyKivyApp().run()
