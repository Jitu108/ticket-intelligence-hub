# ui/app.py
import gradio as gr
from ticket_hub.infrastructure.db import DbConnectionProvider, UnitOfWork
from ticket_hub.application.services import TicketService
from ticket_hub.application.dtos import CreateTicketDTO
from ticket_hub.infrastructure.llm import llm_factory
from ticket_hub.infrastructure.embedding import OpenAIEmbedding
from ticket_hub.config import settings

provider = DbConnectionProvider(settings.SQLSERVER_CONN_STR)
service = TicketService(
    llm=llm_factory(settings.LLM_PROVIDER, settings.LLM_MODEL),
    embedder=OpenAIEmbedding(settings.EMBED_MODEL)
)

def create_ticket_ui(email, subject, body):
    with UnitOfWork(provider) as conn:
        tid = service.create_ticket(conn, CreateTicketDTO(
            requester_email=email, subject=subject, body=body))
    return f"Ticket #{tid} created."

def view_ticket_ui(ticket_id):
    with UnitOfWork(provider) as conn:
        dto = service.view_ticket(conn, int(ticket_id))
    return dto.model_dump_json(indent=2)

def summarize_ui(ticket_id) -> tuple[str, str]:
    with UnitOfWork(provider) as conn:
        messages, summary = service.summarize_ticket(conn, int(ticket_id))
    return messages, summary

with gr.Blocks(title="Ticket Intelligence Hub") as demo:
    gr.Markdown("# Ticket Intelligence Hub (OOP)")
    with gr.Tab("Create"):
        email = gr.Textbox(label="Requester Email")
        subject = gr.Textbox(label="Subject")
        body = gr.Textbox(label="Body", lines=6)
        out = gr.Textbox(label="Result")
        gr.Button("Create Ticket").click(create_ticket_ui, [email, subject, body], out)

    with gr.Tab("View"):
        tid = gr.Number(label="Ticket ID")
        out_view = gr.Textbox(label="Ticket JSON", lines=16)
        gr.Button("Load").click(view_ticket_ui, [tid], out_view)

    with gr.Tab("Summarize"):
        tid2 = gr.Number(label="Ticket ID")
        orig_msgs_out = gr.Textbox(label="Original Messages", lines=10, interactive=False)
        sum_out = gr.Textbox(label="LLM Summary", lines=10)
        gr.Button("Generate Summary").click(
            summarize_ui, 
            [tid2], 
            outputs=[orig_msgs_out, sum_out])

demo.launch()