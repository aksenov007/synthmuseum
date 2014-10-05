from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Module(models.Model):
    # Choices must be added
    manufacturer = models.CharField(max_length=16)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.manufacturer + ' ' + self.name
    def determine(self):
        if hasattr(self, 'oscillator'):
            return 'Oscillator'
        elif hasattr(self, 'noisegenerator'):
            return 'Noise generator'
        elif hasattr(self, 'amplifier'):
            return 'Amplifier'
        elif hasattr(self, 'filter'):
            return 'Filter'
        elif hasattr(self, 'keyboard'):
            return 'Keyboard'
        else:
            return 'Envelope generator'

class Waveform(models.Model):
    WAVEFORM_TYPES = (
        ('si', 'Sine'),
        ('tr', 'Triangular'),
        ('pu', 'Pulse'),
        ('sa', 'Sawtooth'),
        ('sq', 'Square')
        )
    name = models.CharField(max_length=2, choices=WAVEFORM_TYPES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Oscillator(Module):
    OSCILLATOR_TYPES = (
        ('VCO', 'Voltage Controlled Oscillator'),
        ('DCO', 'Digitally Controlled Oscillator'),
        ('PCM', 'Pulse Code Modulation'),
        ('NCO', 'Numerically Controlled Oscillator')
        )
    LFO_mode = (
        (1, 'Yes'),
        (2, 'No'),
        (3, 'Only LFO')
        )
    type = models.CharField(max_length=3, choices=OSCILLATOR_TYPES)
    waveforms = models.ManyToManyField(Waveform)
    LFO = models.PositiveSmallIntegerField(choices=LFO_mode)
    sub_oscillator = models.BooleanField(default=False)
    env_mod_pitch = models.BooleanField(default=False)
    LFO_mod_pitch = models.BooleanField(default=False)
    LFO_mod_pulse_width = models.BooleanField(default=False)
    key_track_pitch = models.BooleanField(default=False)        
    
class Noise(models.Model):
    NOISE_TYPES = (
        ('w', 'White'),
        ('p', 'Pink'),
        ('g', 'Grey'),
        ('f', 'Flicker'),
        ('b', 'Brown/Red')
        )
    name = models.CharField(max_length=1, choices=NOISE_TYPES, unique=True)

    def __str__(self):
        return self.get_name_display()
    
class NoiseGenerator(Module):
    noise_types = models.ManyToManyField(Noise)

class Amplifier(Module):
    AMPLIFIER_TYPES = (
        ('VCA', 'Voltage Controlled Amplifier'),
        ('DCA', 'Digitally Controlled Amplifier'),
        ('TVA', 'Time Variant Amplifier'),
        ('VDA', 'Variable Digital Amplifier')
        )
    type = models.CharField(max_length=3, choices=AMPLIFIER_TYPES)
    key_track_mod_amp_env = models.BooleanField(default=False)
    LFO_mod = models.BooleanField(default=False)
    vel_mod_amp = models.BooleanField(default=False)
    vel_mod_attack = models.BooleanField(default=False)

class EnvelopeGenerator(Module):
    ADSR_TYPES = (
        ('ADSR', 'Attack, Decay, Sustain, Release'),
        ('ADS', 'Attack, Decay, Sustain'),
        ('ADBDSR', 'Attack, Decay-1, Break-Point, Decay-2, Sustain, Release')
        )
    type = models.CharField(max_length=6, choices=ADSR_TYPES)

class FilterPole(models.Model):
    FILTER_POLES = (
        (6, '1-pole/6dB per octave'),
        (12, '2-pole/12dB per octave'),
        (18, '3-pole/18dB per octave'),
        (24, '4-pole/24dB per octave')
        )
    type = models.PositiveSmallIntegerField(choices=FILTER_POLES, unique=True)
    
    def __str__(self):
        return self.get_type_display()

class Filter(Module):
    FILTER_KINDS = (
        ('LPF', 'Low-Pass Filter'),
        ('HPF', 'High-Pass Filter'),
        ('BRF', 'Band-Reject Filter'),
        ('BPF', 'Band-Pass Filter')
        )
    FILTER_TYPES = (
        ('VCF', 'Voltage Controlled Filter'),
        ('DCF', 'Digitally Controlled Filter'),
        ('TVF', 'Time Variant Filter'),
        ('VDF', 'Variable Digital Filter')
        )
    type = models.CharField(max_length=3, choices=FILTER_TYPES)
    kind = models.CharField(max_length=3, choices=FILTER_KINDS)
    poles = models.ManyToManyField(FilterPole)
    resonance = models.BooleanField(default=False)
    env_mod_cut_off = models.BooleanField(default=False)
    env_amount = models.BooleanField(default=False)
    LFO_mod = models.BooleanField(default=False)
    key_track_cut_off = models.BooleanField(default=False)
    vel_mod_cut_off = models.BooleanField(default=False)
    vel_mod_cut_off_env = models.BooleanField(default=False)

class Keyboard(Module):
    KEYBOARD_TYPES = (
        (1, 'Standard'),
        (2, 'Capacitance-touch-sensitive')
        )
    STIFFNESS_TYPES = (
        (1, 'Not weighted'),
        (2, 'Semi-weighted'),
        (3, 'Weighted')
        )
    KEY_SIZES = (
        (True, 'Standard'),
        (False, 'Small')
        )
    count = models.PositiveSmallIntegerField()
    type = models.PositiveSmallIntegerField(choices=KEYBOARD_TYPES)
    velocity = models.BooleanField(default=False)
    aftertouch = models.BooleanField(default=False)
    polyphony = models.PositiveSmallIntegerField(default=1, null=True)
    pitch = models.BooleanField(default=True)
    modulation = models.BooleanField(default=True)
    transpose = models.BooleanField(default=False)
    portamento = models.BooleanField(default=False)
    zones = models.BooleanField(default=1)
    arpeggiator = models.BooleanField(default=False)
    joystick = models.BooleanField(default=False)
    ribbon = models.BooleanField(default=False)
    stiffness = models.PositiveSmallIntegerField(choices=STIFFNESS_TYPES)
    hammer_action = models.BooleanField(default=False)
    key_size = models.BooleanField(choices=KEY_SIZES, default=True)

class Effect(models.Model):
    EFFECT_TYPES = (
        (1, 'Delay'),
        (2, 'Chorus'),
        (3, 'Reverb'),
        (4, 'Overdrive'),
        (5, 'Flanger'),
        (6, 'Phaser')
        )
    type = models.PositiveSmallIntegerField(choices=EFFECT_TYPES, unique=True)
    
    def __str__(self):
        return self.get_type_display()

MARKS = (
    (1, 'Garbage'),
    (2, 'Humdrum'),
    (3, 'Good'),
    (4, 'Excellent'),
    (5, 'Awesome!')
)

class Synthesizer(models.Model):
    # Choices must be added
    manufacturer = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    rating_site = models.PositiveSmallIntegerField(choices=MARKS)
    rating_user = models.FloatField(null=True, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    modules = models.ManyToManyField(Module)
    description = models.TextField(default='Please, enter some description...')

    def __str__(self):
        return self.manufacturer + ' ' + self.name

class Protocol(models.Model):
    PROTOCOL_TYPES = (
        (1, 'MIDI'),
        (2, 'CV/Gate')
        )
    type = models.PositiveSmallIntegerField(choices=PROTOCOL_TYPES)

    def __str__(self):
        return self.get_type_display()

class StandardSynthesizer(Synthesizer):
    SYNTHESIS_TYPES = (
        ('Sub', 'Subtractive'),
        ('Add', 'Additive'),
        ('WT', 'Wavetable'),
        ('FM', 'Frequency Modulation'),
        ('PD', 'Phase Distortion'),
        ('PM', 'Physical Modelling'),
        ('PCM', 'Pulse Code Modulation'),
        ('LA', 'Linear-Arithmetic')
        )
    synthesis_type = models.CharField(max_length=3, choices=SYNTHESIS_TYPES)
    protocols = models.ManyToManyField(Protocol)
    metronome = models.BooleanField(default=False)
    polyphony = models.PositiveIntegerField(null=False)
    vocoder = models.BooleanField(default=False)
    built_in_speaker = models.BooleanField(default=False)
    built_in_speaker_power = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    display = models.BooleanField(default=False)
    USB = models.BooleanField(default=False)
    height = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    depth = models.PositiveSmallIntegerField()
    weight = models.FloatField()
