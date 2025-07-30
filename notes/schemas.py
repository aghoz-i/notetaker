from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from .serializers import NoteSerializer

note_list_get_schema = extend_schema(
    summary="List all notes",
    description="Retrieve a list of all notes.",
    responses={
        200: OpenApiResponse(
            description="Successful retrieval of notes",
            response=NoteSerializer(many=True),
            examples=[
                OpenApiExample(
                    name="Example notes response",
                    value={
                        "id": 1,
                        "title": "Note 1",
                        "content": "This is the content of note 1.\nYes it is.\nWhat?\nNo this is the content.",
                        "created_at": "2025-07-30T10:00:00Z",
                        "updated_at": "2025-07-30T10:00:00Z"
                    },
                ),
            ]
        ),
    },
)

note_list_post_schema = extend_schema(
    summary="Create a new note",
    description="Add a new note.",
    request=NoteSerializer,
    examples=[
        OpenApiExample(
            name="Create meeting note",
            request_only=True,
            value={
                "title": "Weekly Team Meeting",
                "content": "Agenda:\n1. Project updates\n2. Sprint planning\n3. Code review process\n4. Next week's goals"
            }
        ),
    ],
    responses={
        201: OpenApiResponse(
            description="Successful creation of new note",
            response=NoteSerializer,
            examples=[
                OpenApiExample(
                    name="Created note response",
                    response_only=True,
                    value={
                        "id": 15,
                        "title": "Weekly Team Meeting",
                        "content": "Agenda:\n1. Project updates\n2. Sprint planning\n3. Code review process\n4. Next week's goals",
                        "created_at": "2025-07-30T14:30:00Z",
                        "updated_at": "2025-07-30T14:30:00Z"
                    }
                )
            ]
        ),
        400: OpenApiResponse(
            description="Invalid data",
        ),
    },
)

note_detail_get_schema = extend_schema(
    summary="Retrieve a note",
    description="Get the details of a specific note by its ID.",
    responses={
        200: OpenApiResponse(
            description="Successful retrieval of note details",
            response=NoteSerializer,
            examples=[
                OpenApiExample(
                    name="Note details response",
                    value={
                        "id": 5,
                        "title": "El-Noted",
                        "content": "Noted will be noted of the note in the note.",
                        "created_at": "2025-07-28T16:45:00Z",
                        "updated_at": "2025-07-30T09:22:00Z"
                    }
                )
            ]
        ),
        404: OpenApiResponse(description="Note not found"),
    },
)

note_detail_put_schema = extend_schema(
    summary="Update a note",
    description="Update an existing note by its ID.",
    request=NoteSerializer,
    examples=[
        OpenApiExample(
            name="Update note content",
            request_only=True,
            value={
                "title": "This is an updated note title",
                "content": "And this is the updated note content.",
            }
        )
    ],
    responses={
        200: OpenApiResponse(
            description="Successful update of note",
            response=NoteSerializer,
            examples=[
                OpenApiExample(
                    name="Updated note response",
                    response_only=True,
                    value={
                        "id": 5,
                        "title": "This is an updated note title",
                        "content": "And this is the updated note content.",
                        "created_at": "2025-07-28T16:45:00Z",
                        "updated_at": "2025-07-30T15:10:00Z"
                    }
                )
            ]
        ),
        400: OpenApiResponse(description="Invalid data"),
        404: OpenApiResponse(description="Note not found"),
    },
)

note_detail_delete_schema = extend_schema(
    summary="Delete a note",
    description="Delete a specific note by its ID.",
    responses={
        204: OpenApiResponse(description="Note deleted successfully"),
        404: OpenApiResponse(description="Note not found"),
    },
)

            