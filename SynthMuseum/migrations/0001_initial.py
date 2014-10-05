# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.PositiveSmallIntegerField(unique=True, choices=[(1, 'Delay'), (2, 'Chorus'), (3, 'Reverb'), (4, 'Overdrive'), (5, 'Flanger'), (6, 'Phaser')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FilterPole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('module_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SynthMuseum.Module')),
                ('count', models.PositiveSmallIntegerField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Standard'), (2, 'Capacitance-touch-sensitive')])),
                ('velocity', models.BooleanField(default=False)),
                ('aftertouch', models.BooleanField(default=False)),
                ('polyphony', models.PositiveSmallIntegerField(default=1, null=True)),
                ('pitch', models.BooleanField(default=True)),
                ('modulation', models.BooleanField(default=True)),
                ('transpose', models.BooleanField(default=False)),
                ('portamento', models.BooleanField(default=False)),
                ('zones', models.BooleanField(default=1)),
                ('arpeggiator', models.BooleanField(default=False)),
                ('joystick', models.BooleanField(default=False)),
                ('ribbon', models.BooleanField(default=False)),
                ('stiffness', models.PositiveSmallIntegerField(choices=[(1, 'Not weighted'), (2, 'Semi-weighted'), (3, 'Weighted')])),
                ('hammer_action', models.BooleanField(default=False)),
                ('key_size', models.BooleanField(default=True, choices=[(True, 'Standard'), (False, 'Small')])),
            ],
            options={
            },
            bases=('SynthMuseum.module',),
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('module_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SynthMuseum.Module')),
                ('type', models.CharField(max_length=3, choices=[('VCF', 'Voltage Controlled Filter'), ('DCF', 'Digitally Controlled Filter'), ('TVF', 'Time Variant Filter'), ('VDF', 'Variable Digital Filter')])),
                ('kind', models.CharField(max_length=3, choices=[('LPF', 'Low-Pass Filter'), ('HPF', 'High-Pass Filter'), ('BRF', 'Band-Reject Filter'), ('BPF', 'Band-Pass Filter')])),
                ('resonance', models.BooleanField(default=False)),
                ('env_mod_cut_off', models.BooleanField(default=False)),
                ('env_amount', models.BooleanField(default=False)),
                ('LFO_mod', models.BooleanField(default=False)),
                ('key_track_cut_off', models.BooleanField(default=False)),
                ('vel_mod_cut_off', models.BooleanField(default=False)),
                ('vel_mod_cut_off_env', models.BooleanField(default=False)),
                ('poles', models.ManyToManyField(to='SynthMuseum.FilterPole')),
            ],
            options={
            },
            bases=('SynthMuseum.module',),
        ),
        migrations.CreateModel(
            name='EnvelopeGenerator',
            fields=[
                ('module_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SynthMuseum.Module')),
                ('type', models.CharField(max_length=6, choices=[('ADSR', 'Attack, Decay, Sustain, Release'), ('ADS', 'Attack, Decay, Sustain'), ('ADBDSR', 'Attack, Decay-1, Break-Point, Decay-2, Sustain, Release')])),
            ],
            options={
            },
            bases=('SynthMuseum.module',),
        ),
        migrations.CreateModel(
            name='Amplifier',
            fields=[
                ('module_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SynthMuseum.Module')),
                ('type', models.CharField(max_length=3, choices=[('VCA', 'Voltage Controlled Amplifier'), ('DCA', 'Digitally Controlled Amplifier'), ('TVA', 'Time Variant Amplifier'), ('VDA', 'Variable Digital Amplifier')])),
                ('key_track_mod_amp_env', models.BooleanField(default=False)),
                ('LFO_mod', models.BooleanField(default=False)),
                ('vel_mod_amp', models.BooleanField(default=False)),
                ('vel_mod_attack', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('SynthMuseum.module',),
        ),
        migrations.CreateModel(
            name='Noise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1, choices=[('w', 'White'), ('p', 'Pink'), ('g', 'Grey'), ('f', 'Flicker'), ('b', 'Brown/Red')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoiseGenerator',
            fields=[
                ('module_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SynthMuseum.Module')),
                ('noise_types', models.ManyToManyField(to='SynthMuseum.Noise')),
            ],
            options={
            },
            bases=('SynthMuseum.module',),
        ),
        migrations.CreateModel(
            name='Oscillator',
            fields=[
                ('module_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SynthMuseum.Module')),
                ('type', models.CharField(max_length=3, choices=[('VCO', 'Voltage Controlled Oscillator'), ('DCO', 'Digitally Controlled Oscillator'), ('PCM', 'Pulse Code Modulation'), ('NCO', 'Numerically Controlled Oscillator')])),
                ('LFO', models.PositiveSmallIntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, 'Only LFO')])),
                ('sub_oscillator', models.BooleanField(default=False)),
                ('env_mod_pitch', models.BooleanField(default=False)),
                ('LFO_mod_pitch', models.BooleanField(default=False)),
                ('LFO_mod_pulse_width', models.BooleanField(default=False)),
                ('key_track_pitch', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('SynthMuseum.module',),
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'MIDI'), (2, 'CV/Gate')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Synthesizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=8)),
                ('rating_site', models.PositiveSmallIntegerField(choices=[(1, 'Garbage'), (2, 'Humdrum'), (3, 'Good'), (4, 'Excellent'), (5, 'Awesome!')])),
                ('rating_user', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardSynthesizer',
            fields=[
                ('synthesizer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SynthMuseum.Synthesizer')),
                ('synthesis_type', models.CharField(max_length=3, choices=[('Sub', 'Subtractive'), ('Add', 'Additive'), ('WT', 'Wavetable'), ('FM', 'Frequency Modulation'), ('PD', 'Phase Distortion'), ('PM', 'Physical Modelling'), ('PCM', 'Pulse Code Modulation'), ('LA', 'Linear-Arithmetic')])),
                ('metronome', models.BooleanField(default=False)),
                ('polyphony', models.PositiveIntegerField()),
                ('vocoder', models.BooleanField(default=False)),
                ('built_in_speaker', models.BooleanField(default=False)),
                ('built_in_speaker_power', models.DecimalField(max_digits=5, decimal_places=2)),
                ('display', models.BooleanField(default=False)),
                ('USB', models.BooleanField(default=False)),
                ('height', models.PositiveSmallIntegerField()),
                ('width', models.PositiveSmallIntegerField()),
                ('depth', models.PositiveSmallIntegerField()),
                ('weight', models.FloatField()),
                ('protocols', models.ManyToManyField(to='SynthMuseum.Protocol')),
            ],
            options={
            },
            bases=('SynthMuseum.synthesizer',),
        ),
        migrations.CreateModel(
            name='Waveform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=2, choices=[('si', 'Sine'), ('tr', 'Triangular'), ('pu', 'Pulse'), ('sa', 'Sawtooth'), ('sq', 'Square')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='synthesizer',
            name='modules',
            field=models.ManyToManyField(to='SynthMuseum.Module'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oscillator',
            name='waveforms',
            field=models.ManyToManyField(to='SynthMuseum.Waveform'),
            preserve_default=True,
        ),
    ]
