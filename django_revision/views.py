from django_revision.revision import Revision


class RevisionMixin:

    def get_context_data(self, **kwargs):
        context = super(RevisionMixin, self).get_context_data(**kwargs)
        revision = Revision()
        context.update({
            'revision': revision.tag or revision.commit,
        })
        return context
