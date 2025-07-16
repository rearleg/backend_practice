from django.contrib import admin
from .models import Tweet, Like


class ContainElonMusk(admin.SimpleListFilter):
    title = "Contain Elon Musk?"
    parameter_name = "elon"

    def lookups(self, request, model_admin):
        return [
            ("musk", "Musk"),
            ("not_musk", "Not_Musk"),
        ]

    def queryset(self, request, elon_musk):
        musk = self.value()
        if musk == "musk":
            return elon_musk.filter(payload__icontains="Elon Musk")
        elif musk == "not_musk":
            return elon_musk.exclude(payload__icontains="Elon Musk")
        else:
            elon_musk

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "like_count",
    )

    list_filter = (
        ContainElonMusk,
        "created_at",
    )

    search_fields = (
        "payload",
        "user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
    )

    search_fields = ("user__username",)

    list_filter = ("created_at",)
