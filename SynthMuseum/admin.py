from django.contrib import admin
from SynthMuseum.models import Module, Oscillator, NoiseGenerator, Amplifier, EnvelopeGenerator, Filter, Keyboard, Synthesizer, StandardSynthesizer

admin.site.register(Oscillator)
admin.site.register(NoiseGenerator)
admin.site.register(Amplifier)
admin.site.register(EnvelopeGenerator)
admin.site.register(Filter)
admin.site.register(Keyboard)
admin.site.register(Synthesizer)

class StandardSynthesizerAdmin(admin.ModelAdmin):
    fields = ['manufacturer', 'name', 'rating_site', 'description', 'modules', 'synthesis_type', 'protocols', 'metronome', 'polyphony', 'vocoder', 'built_in_speaker', 'built_in_speaker_power', 'display', 'USB', 'height', 'width', 'depth', 'weight']
admin.site.register(StandardSynthesizer, StandardSynthesizerAdmin)
