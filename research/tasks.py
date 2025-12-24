from celery import shared_task
from .ai.runner import run_research
from .models import *

@shared_task
def run_research_task(research_id):
    research = ResearchSession.objects.get(id=research_id)

    result, trace_id = run_research(research.query)

    ResearchSummary.objects.update_or_create(
        research=research,
        defaults={"summary": result["summary"]}
    )

    ResearchReasoning.objects.update_or_create(
        research=research,
        defaults={"reasoning": result["reasoning"]}
    )

    ResearchCost.objects.update_or_create(
        research=research,
        defaults={"input_tokens": 500, "output_tokens": 800, "total_cost": 0.02}
    )

    research.status = "COMPLETED"
    research.trace_id = trace_id
    research.save()
