import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

TabelaFases = []


class DBFases:
    DB_Fases = [["Cadastro  ", "Planejamento                      ",
                 "20/05/2025", "22/05/2025"],
                ["Licitação ", "Ficha Demanda                     ",
                 "21/05/2025", "22/05/2025"],
                ["Licitação ", "Estudo Técnico Preliminar         ",
                 "23/05/2025", ""],
                ["Licitação ", "Matriz de Risco                   ",
                 "", ""],
                ["Licitação ", "Termo Referencia                  ",
                 "", ""],
                ["Licitação ", "Cotação                           ",
                 "", ""],
                ["Licitação ", "Reserva Orçamentária              ",
                 "", ""],
                ["Licitação ", "Edital e Anexos                   ",
                 "", ""],
                ["Licitação ", "Parecer Jurídico                  ",
                 "", ""],
                ["Licitação ", "Autorização da Ordem de Despesa   ",
                 "", ""],
                ]


def fases():
    form_frame = tk.LabelFrame(
        frame_tabela, text="Preencha as Fases", padx=10, pady=10)
    form_frame.pack(padx=10, pady=10, fill="x")

    headers = ["Fase", "Data Início", "Data Fim"]
    for col, text in enumerate(headers):
        tk.Label(form_frame, text=text, font=("Arial", 10, "bold")).grid(
            row=0, column=col, padx=5, pady=5)

    for i in range(10):
        row_entries = []

        fase = tk.Entry(form_frame, width=25)
        fase.grid(row=i+1, column=0, padx=5, pady=2)
        fase.insert(0, f"{DBFases.DB_Fases[i][0]} {DBFases.DB_Fases[i][1]}")
        row_entries.append(fase)

        data_inicio = DateEntry(form_frame, width=18,
                                date_pattern="dd/mm/yyyy")
        data_inicio.grid(row=i+1, column=1, padx=5, pady=2)
        data_inicio.delete(0, tk.END)
        if DBFases.DB_Fases[i][2]:
            data_inicio.set_date(DBFases.DB_Fases[i][2])
        row_entries.append(data_inicio)

        data_fim = DateEntry(form_frame, width=18, date_pattern="dd/mm/yyyy")
        data_fim.grid(row=i+1, column=2, padx=5, pady=2)
        data_fim.delete(0, tk.END)
        if DBFases.DB_Fases[i][3]:
            data_fim.set_date(DBFases.DB_Fases[i][3])
        row_entries.append(data_fim)

        TabelaFases.append(row_entries)

    btn_frame = tk.Frame(frame_tabela)
    btn_frame.pack(padx=10, pady=10)

    save_btn = tk.Button(
        frame_tabela, text="Salvar na Tabela", command=save_entries)
    save_btn.pack()


def save_entries():
    i = 0
    for row in TabelaFases:
        DBFases.DB_Fases[i][2] = row[1].get()
        DBFases.DB_Fases[i][3] = row[2].get()
        if DBFases.DB_Fases[i][2]:
            print(DBFases.DB_Fases[i][0])
            print(DBFases.DB_Fases[i][1])
            print(DBFases.DB_Fases[i][2])
            print(DBFases.DB_Fases[i][3])
            print("--------------")
        i = i+1


janela = tk.Tk()
janela.title("Exemplo de Tabela com SELECT")

frame_tabela = tk.Frame(janela)
frame_tabela.pack(padx=10, pady=10)

# table_frame = tk.LabelFrame(frame_tabela, text="Fases Cadastradas", padx=10, pady=10)

fases()

janela.mainloop()
