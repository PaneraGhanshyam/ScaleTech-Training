from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from .models import Document


@login_required
@permission_required(
    "documents.view_document",
    raise_exception=True,
)
def document_list(request):

    documents = Document.objects.select_related(
        "created_by"
    )

    return render(
        request,
        "documents/list.html",
        {"documents": documents},
    )