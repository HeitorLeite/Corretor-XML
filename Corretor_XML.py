"""
Corretor de Procedimentos TISS XML - Unimed

Detecta procedimentos com prefixo incorreto (19 ou 20)
quando codigoTabela = 00 e corrige automaticamente.


Desenvolvido por: Heitor Leite - 2026
"""

import re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

conteudo_xml = ""
erros = []

# -----------------------------
# Selecionar arquivo XML
# -----------------------------
def selecionar_xml():

    caminho = filedialog.askopenfilename(
        title="Selecione o XML",
        filetypes=[("Arquivos XML", "*.xml")]
    )

    if caminho:
        entrada_var.set(caminho)


# -----------------------------
# Selecionar local de saída
# -----------------------------
def selecionar_saida():

    caminho = filedialog.asksaveasfilename(
        title="Salvar XML corrigido",
        defaultextension=".xml",
        filetypes=[("Arquivos XML", "*.xml")]
    )

    if caminho:
        saida_var.set(caminho)


# -----------------------------
# Analisar XML
# -----------------------------
def analisar():

    global conteudo_xml
    global erros

    erros.clear()

    caminho = entrada_var.get()

    if not caminho:
        messagebox.showwarning("Aviso", "Selecione um arquivo XML")
        return

    with open(caminho, "r", encoding="utf-8") as f:
        conteudo_xml = f.read()

    padrao = re.compile(
        r"(<ans:codigoTabela>00</ans:codigoTabela>\s*<ans:codigoProcedimento>)(19|20)(\d+)(</ans:codigoProcedimento>)"
    )

    for item in tabela.get_children():
        tabela.delete(item)

    for match in padrao.finditer(conteudo_xml):

        posicao = match.start()
        original = match.group(2) + match.group(3)
        corrigido = match.group(3)

        erros.append((posicao, original, corrigido))

        tabela.insert("", "end", values=(posicao, original, corrigido))

    total_var.set(f"Erros encontrados: {len(erros)}")

    if len(erros) == 0:
        messagebox.showinfo("Resultado", "Nenhum erro encontrado no XML.")


# -----------------------------
# Corrigir XML
# -----------------------------
def corrigir():

    global conteudo_xml

    if len(erros) == 0:
        messagebox.showwarning("Aviso", "Nenhum erro para corrigir.")
        return

    caminho_saida = saida_var.get()

    if not caminho_saida:
        messagebox.showwarning("Aviso", "Selecione onde salvar o XML corrigido")
        return

    confirmar = messagebox.askyesno(
        "Confirmação",
        f"Serão corrigidos {len(erros)} procedimentos.\nDeseja continuar?"
    )

    if not confirmar:
        return

    padrao = re.compile(
        r"(<ans:codigoTabela>00</ans:codigoTabela>\s*<ans:codigoProcedimento>)(19|20)(\d+)(</ans:codigoProcedimento>)"
    )

    def substituir(match):
        return match.group(1) + match.group(3) + match.group(4)

    conteudo_corrigido = padrao.sub(substituir, conteudo_xml)

    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(conteudo_corrigido)

    messagebox.showinfo("Sucesso", "XML corrigido salvo com sucesso!")


# -----------------------------
# Interface gráfica
# -----------------------------

janela = tk.Tk()
janela.title("Corretor XML TISS - Unimed")
janela.geometry("750x500")

entrada_var = tk.StringVar()
saida_var = tk.StringVar()
total_var = tk.StringVar()

# Seleção de arquivo
frame_top = tk.Frame(janela)
frame_top.pack(pady=10)

tk.Label(frame_top, text="XML de Entrada").grid(row=0, column=0, padx=5)

tk.Entry(frame_top, textvariable=entrada_var, width=60).grid(row=0, column=1)

tk.Button(frame_top, text="Selecionar", command=selecionar_xml).grid(row=0, column=2, padx=5)

# Saída
tk.Label(frame_top, text="XML Corrigido").grid(row=1, column=0, padx=5)

tk.Entry(frame_top, textvariable=saida_var, width=60).grid(row=1, column=1)

tk.Button(frame_top, text="Salvar em...", command=selecionar_saida).grid(row=1, column=2, padx=5)

# Botão analisar
tk.Button(
    janela,
    text="Analisar XML",
    command=analisar,
    height=2,
    width=20
).pack(pady=10)

# Tabela de erros
colunas = ("Posição no XML", "Código Original", "Código Corrigido")

tabela = ttk.Treeview(janela, columns=colunas, show="headings")

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=200)

tabela.pack(expand=True, fill="both", padx=20, pady=10)

# Total de erros
tk.Label(janela, textvariable=total_var, font=("Arial", 12)).pack()

# Botão corrigir
tk.Button(
    janela,
    text="Corrigir e Salvar XML",
    command=corrigir,
    bg="#2ecc71",
    fg="white",
    height=2,
    width=25
).pack(pady=15)

janela.mainloop()