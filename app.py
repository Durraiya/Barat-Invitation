
import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="Durraiya & Hammad | Barat",
    page_icon="✨",
    layout="wide"
)

html = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&family=Noto+Naskh+Arabic:wght@400;500;600;700&family=Amiri:wght@400;700&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --emerald: #263D35;
    --emerald-light: #385747;
    --sage: #536B55;
    --sage-pale: #E8EDE4;
    --ivory: #F8F5EC;
    --antique-gold: #B99A62;
    --gold-light: #D2B77F;
}

html, body {
    width: 100%;
    overflow-x: hidden;
}

body {
    background: radial-gradient(
        ellipse at 50% 0%,
        #F8F5EC 0%,
        #EEEBDD 55%,
        #E3E7DC 100%
    );
    color: var(--emerald);
    font-family: 'Cormorant Garamond', serif;
}

#fallingPetals {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
    opacity: 1;
}

.page {
    position: relative;
    z-index: 1;
    max-width: 900px;
    margin: 30px auto;
    padding: 16px;
    background: rgba(248,245,236,0.12);
    border: 2px solid var(--antique-gold);
    box-shadow: 0 12px 45px rgba(38,61,53,.13);
}

.inner {
    position: relative;
    border: 1px solid var(--antique-gold);
    padding: 35px 24px;
    text-align: center;
    background: transparent;
}

.inner > * {
    position: relative;
    z-index: 3;
}

.section-card {
    position: relative;
    isolation: isolate;
    background: transparent;
    border: 1px solid var(--antique-gold);
    border-radius: 5px;
    padding: 30px 22px;
    margin: 25px auto;
    max-width: 760px;
    box-shadow:
        0 7px 24px rgba(38,61,53,.08),
        inset 0 0 24px rgba(185,154,98,.06);
}

.section-card::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 0;
    background: rgba(248,245,236,0.62);
    border-radius: inherit;
    pointer-events: none;
}

.section-card > * {
    position: relative;
    z-index: 3;
}

.top-label {
    color: var(--sage);
    font-size: 14px;
    letter-spacing: 5px;
    text-transform: uppercase;
    margin-bottom: 25px;
}

.bismillah {
    color: var(--emerald);
    font-family: 'Amiri', serif;
    font-size: 30px;
    margin: 15px 0 30px;
}

.intro {
    color: #53634F;
    font-size: 22px;
    line-height: 1.8;
    max-width: 680px;
    margin: 0 auto 25px;
}

.intro strong {
    color: var(--emerald);
    font-weight: 700;
}

.couple-name {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(42px, 6vw, 50px);
    font-weight: 400;
    line-height: 1.35;
    display: block;
    margin: 8px auto;
    color: var(--emerald);
    text-shadow: 0 1px 0 rgba(255,255,255,.75);
}

.family {
    color: #53634F;
    font-size: 19px;
    line-height: 1.6;
    margin: 10px auto 20px;
}

.with {
    color: var(--antique-gold);
    font-size: 25px;
    font-style: italic;
    margin: 15px 0;
}

.couple-card {
    overflow: hidden;
}

.couple-layout {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(210px, .72fr);
    align-items: center;
    gap: 10px;
}

.couple-copy {
    min-width: 0;
}

.illustration-wrap {
    width: 100%;
    max-width: 300px;
    justify-self: end;
    line-height: 0;
}

.couple-illustration {
    display: block;
    width: 100%;
    height: auto;
    object-fit: contain;
    filter: drop-shadow(0 7px 10px rgba(85,42,35,.10));
}

.event-label {
    color: var(--sage);
    letter-spacing: 5px;
    font-size: 20px;
    margin-top: 10px;
}

.event-title {
    color: var(--emerald);
    font-size: 48px;
    margin: 12px 0 8px;
    letter-spacing: 6px;
    font-weight: 600;
}

.inshallah {
    color: var(--emerald);
    font-family: 'Amiri', serif;
    font-size: 32px;
    font-weight: 400;
    direction: rtl;
    margin: 8px 0 20px;
}

.date-card {
    display: inline-block;
    border: 1px solid var(--antique-gold);
    padding: 22px 40px;
    margin: 15px 0 25px;
    background: rgba(232,237,228,.88);
    box-shadow: 0 5px 18px rgba(110,65,47,.08);
}

.date {
    font-size: 35px;
    color: var(--emerald);
}

.time {
    color: #53634F;
    font-size: 22px;
    margin-top: 8px;
}

.countdown-heading {
    color: var(--sage);
    font-size: 20px;
    letter-spacing: 3px;
    margin: 25px 0 15px;
}

.countdown {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
    margin: 20px auto 5px;
}

.time-box {
    min-width: 90px;
    padding: 15px 10px;
    border: 1px solid var(--antique-gold);
    background: rgba(232,237,228,.88);
    border-radius: 4px;
}

.time-number {
    color: var(--emerald);
    font-size: 35px;
    display: block;
}

.time-unit {
    color: #687B65;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.venue-heading {
    color: var(--sage);
    font-size: 20px;
    letter-spacing: 4px;
}

.venue-name {
    font-size: 32px;
    color: var(--emerald);
    margin: 12px 0;
}

.venue-address {
    color: #53634F;
    font-size: 19px;
    line-height: 1.5;
}

.map-link,
.whatsapp-btn,
.send-btn {
    display: inline-block;
    padding: 13px 25px;
    margin-top: 18px;
    background: linear-gradient(
        135deg,
        var(--emerald-light),
        var(--emerald)
    );
    color: #FFFDF5;
    text-decoration: none;
    border: none;
    border-radius: 3px;
    font-family: inherit;
    font-size: 18px;
    font-weight: 600;
    cursor: pointer;
    transition: 0.3s;
}

.map-link:hover,
.whatsapp-btn:hover,
.send-btn:hover {
    box-shadow: 0 0 18px rgba(38,61,53,.25);
    transform: translateY(-2px);
}

.section-title {
    color: var(--emerald);
    font-size: 32px;
    margin: 5px 0 18px;
}

.section-description {
    color: #53634F;
    font-size: 19px;
    line-height: 1.6;
    margin: 10px 0 20px;
}

.contacts {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 15px;
    max-width: 600px;
    margin: 25px auto 0;
}

.contact {
    background: rgba(237,240,231,.90);
    border: 1px solid var(--antique-gold);
    border-radius: 4px;
    padding: 18px 10px;
    transition: 0.3s;
}

.contact:hover {
    background: #E1E9DF;
    box-shadow: 0 0 14px rgba(38,61,53,.10);
}

.contact-name {
    color: var(--emerald);
    font-size: 23px;
}

.contact-number {
    color: #53634F;
    font-size: 17px;
    margin-top: 6px;
}

.contact a {
    color: inherit;
    text-decoration: none;
}

.dua-options {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
}

.dua-option {
    border: 1px solid var(--antique-gold);
    background: rgba(237,240,231,.90);
    color: var(--emerald);
    border-radius: 3px;
    padding: 12px 16px;
    font-family: 'Noto Naskh Arabic', serif;
    font-size: 19px;
    cursor: pointer;
    transition: 0.2s;
}

.dua-option:hover,
.dua-option.selected {
    background: var(--emerald);
    color: #FFFDF5;
}

#duaInput {
    width: 100%;
    max-width: 450px;
    padding: 13px;
    margin-top: 20px;
    background: #FAF8F0;
    color: var(--emerald);
    border: 1px solid var(--antique-gold);
    border-radius: 3px;
    font-family: inherit;
    font-size: 18px;
    outline: none;
}

#duaInput::placeholder {
    color: #84917D;
}

#duaList {
    list-style: none;
    margin-top: 20px;
}

#duaList li {
    color: var(--emerald);
    padding: 10px;
    border-bottom: 1px solid #C8B58E;
    font-size: 19px;
}

.footer {
    border-top: 1px solid var(--antique-gold);
    color: var(--sage);
    padding-top: 22px;
    margin-top: 25px;
    font-size: 17px;
    letter-spacing: 3px;
    line-height: 1.8;
}

.envelope-intro {
    position: fixed;
    inset: 0;
    z-index: 99999;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 40px 20px 20px;
    background: radial-gradient(
        circle at center,
        #F8F5EC,
        #E8EDE4 70%,
        #DCE5D9
    );
    transition: opacity 1s ease, visibility 1s ease;
}

.envelope-intro.hide {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.envelope-scene {
    width: min(88vw, 540px);
    text-align: center;
}

.envelope-heading {
    font-family: 'Great Vibes', cursive;
    color: var(--emerald);
    font-size: clamp(38px, 7vw, 58px);
    margin-bottom: 28px;
}

.envelope {
    position: relative;
    width: 100%;
    aspect-ratio: 1.55;
    background: #F4F0E4;
    border: 1px solid var(--antique-gold);
    box-shadow: 0 18px 45px rgba(38,61,53,.18);
    overflow: hidden;
    perspective: 1000px;
}

.envelope-back {
    position: absolute;
    inset: 0;
    background: linear-gradient(145deg, #F4F0E4, #E4E9DE);
}

.envelope-front {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        35deg,
        #DCE5D9,
        #F8F5EC 55%,
        #E5EBDD
    );
    clip-path: polygon(0 100%, 50% 45%, 100% 100%);
    z-index: 3;
}

.envelope-flap {
    position: absolute;
    inset: 0;
    background: linear-gradient(145deg, #E5EBDD, #F8F5EC);
    clip-path: polygon(0 0, 100% 0, 50% 58%);
    transform-origin: top center;
    transition: transform .9s ease;
    z-index: 4;
    backface-visibility: visible;
}

.wax-seal {
    position: absolute;
    z-index: 5;
    top: 48%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 82px;
    height: 82px;
    border-radius: 50%;
    border: 3px solid var(--antique-gold);
    background: radial-gradient(
        circle at 35% 30%,
        #496B52,
        #263D35 75%
    );
    color: #E8D3A4;
    font-family: 'Great Vibes', cursive;
    font-size: 26px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow:
        0 4px 10px rgba(38,61,53,.35),
        inset 0 0 0 3px rgba(225,195,130,.3);
    cursor: pointer;
    transition: transform .3s ease, opacity .3s ease;
}

.wax-seal:hover {
    transform: translate(-50%, -50%) scale(1.08);
}

.envelope.open .envelope-flap {
    transform: rotateX(180deg);
}

.envelope.open .wax-seal {
    opacity: 0;
    pointer-events: none;
}

.envelope-roses {
    color: var(--antique-gold);
    font-size: 25px;
    letter-spacing: 10px;
    margin-top: 20px;
}

.open-instruction {
    color: var(--sage);
    font-size: 17px;
    letter-spacing: 2px;
    margin-top: 18px;
}

.envelope-names {
    font-family: 'Cormorant Garamond', serif;
    color: var(--emerald);
    font-size: 14px;
    margin-top: 12px;
}

@media(max-width: 600px) {

    .page {
        width: calc(100% - 8px);
        margin: 6px auto;
        padding: 7px;
    }

    .inner {
        padding: 22px 8px;
    }

    .top-label {
        font-size: 11px;
        letter-spacing: 3px;
        margin-bottom: 18px;
    }

    .bismillah {
        font-size: 27px;
        line-height: 1.9;
        margin: 12px 0 22px;
    }

    .intro {
        font-size: 17px;
        line-height: 1.65;
        padding: 0 5px;
        margin-bottom: 18px;
    }

    .section-card {
        width: 100%;
        max-width: 100%;
        padding: 23px 12px;
        margin: 15px auto;
    }

    .couple-layout {
        grid-template-columns: 1fr;
        gap: 5px;
    }

    .couple-copy {
        order: 1;
    }

    .illustration-wrap {
        order: 2;
        width: min(68%, 220px);
        max-width: 220px;
        justify-self: center;
        margin: 4px auto 0;
    }

    .couple-name {
        font-size: 29px;
        line-height: 1.3;
        margin: 7px auto;
    }

    .family {
        font-size: 16px;
        line-height: 1.5;
        margin: 7px auto 14px;
    }

    .with {
        font-size: 21px;
        margin: 8px 0;
    }

    .event-label {
        font-size: 17px;
        letter-spacing: 3px;
        margin-top: 5px;
    }

    .event-title {
        font-size: 37px;
        letter-spacing: 4px;
        margin: 9px 0 6px;
    }

    .inshallah {
        font-size: 27px;
        margin: 6px 0 14px;
    }

    .date-card {
        display: block;
        width: min(100%, 280px);
        margin: 12px auto 18px;
        padding: 14px 8px;
    }

    .date {
        font-size: clamp(22px, 7vw, 27px);
        line-height: 1.35;
    }

    .time {
        font-size: 17px;
        margin-top: 6px;
    }

    .countdown-heading {
        max-width: 270px;
        margin: 18px auto 12px;
        font-size: 15px;
        line-height: 1.5;
        letter-spacing: 2px;
    }

    .countdown {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        width: min(100%, 230px);
        gap: 9px;
        margin: 14px auto 3px;
    }

    .time-box {
        min-width: 0;
        padding: 11px 5px;
    }

    .time-number {
        font-size: 27px;
    }

    .time-unit {
        font-size: 10px;
        letter-spacing: 1.3px;
    }

    .venue-heading {
        font-size: 18px;
        letter-spacing: 3px;
    }

    .venue-name {
        font-size: 25px;
        line-height: 1.35;
        margin: 10px 0;
        overflow-wrap: anywhere;
    }

    .venue-address {
        font-size: 16px;
    }

    .contacts {
        grid-template-columns: 1fr;
        gap: 10px;
        width: min(100%, 330px);
    }

    .contact {
        padding: 14px 10px;
    }

    .contact-name {
        font-size: 21px;
    }

    .contact-number {
        font-size: 16px;
        overflow-wrap: anywhere;
    }

    .section-title {
        font-size: 27px;
        line-height: 1.3;
    }

    .section-description {
        font-size: 16px;
        line-height: 1.55;
    }

    .dua-options {
        gap: 8px;
    }

    .dua-option {
        max-width: 100%;
        padding: 9px 11px;
        font-size: 17px;
        line-height: 1.7;
    }

    #duaInput {
        width: 100%;
        max-width: 100%;
        font-size: 16px;
        padding: 12px 10px;
    }

    #duaList li {
        font-size: 17px;
        overflow-wrap: anywhere;
    }

    .map-link,
    .whatsapp-btn,
    .send-btn {
        max-width: 100%;
        padding: 12px 16px;
        font-size: 16px;
    }

    .footer {
        font-size: 13px;
        letter-spacing: 2px;
        padding: 18px 5px 0;
    }

    .envelope-intro {
        padding: 28px 12px 16px;
    }

    .envelope-scene {
        width: min(100%, 420px);
    }

    .envelope-heading {
        font-size: clamp(36px, 10vw, 48px);
        margin-bottom: 20px;
    }

    .envelope-roses {
        font-size: 21px;
        letter-spacing: 7px;
    }

    .wax-seal {
        width: 69px;
        height: 69px;
        font-size: 22px;
    }

    .open-instruction {
        font-size: 11px;
        letter-spacing: 1.5px;
    }
}

@media(max-width: 380px) {

    .page {
        width: calc(100% - 6px);
        padding: 5px;
    }

    .inner {
        padding: 18px 6px;
    }

    .section-card {
        padding: 20px 9px;
    }

    .event-title {
        font-size: 34px;
    }

    .date {
        font-size: 23px;
    }

    .countdown {
        max-width: 210px;
    }

    .couple-name {
        font-size: 27px;
    }
}

@media(prefers-reduced-motion: reduce) {

    * {
        scroll-behavior: auto !important;
        animation: none !important;
        transition: none !important;
    }
}
</style>
</head>

<body>

<div class="envelope-intro" id="envelopeIntro">
    <div class="envelope-scene">
        <div class="envelope-heading">Tap to Open</div>

        <div class="envelope">
            <div class="envelope-back"></div>
            <div class="envelope-flap"></div>
            <div class="envelope-front"></div>

            <button
                class="wax-seal"
                id="waxSeal"
                aria-label="Open wedding invitation">
                D & H
            </button>
        </div>

        <div class="envelope-roses">❀ ❧ ❀</div>
    </div>
</div>

<canvas id="fallingPetals"></canvas>

<div class="page">
<div class="inner">

<div class="top-label">
    Together with their families
</div>

<div class="bismillah">
    بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
</div>

<p class="intro">
<strong>Mumtaz Begum &amp; Hassan Pasha</strong>
cordially invite you to join them in celebrating the Rukhsati
of their beloved Grand Daughter
</p>

<div class="section-card couple-card">
    <div class="couple-layout">
        <div class="couple-copy">
            <div class="couple-name">
                Durraiya Shareef
            </div>

            <p class="family">
                Daughter of late Asad Ullah Shareef &amp; Ms. Farah Naz
            </p>

            <div class="with">with</div>

            <div class="couple-name">
                Dr. Hammad Zulfiqar
            </div>

            <p class="family">
                Son of Dr. &amp; Mrs. Muhammad Zulfiqar
            </p>
        </div>

        <div class="illustration-wrap">
            <img
                class="couple-illustration"
                src="data:image/png;base64,__ILLUSTRATION_DATA__"
                alt="Hand-painted bride and groom surrounded by burgundy roses and green leaves">
        </div>
    </div>
</div>

<div class="section-card">
    <div class="event-label">SAVE THE DATE</div>
    <div class="event-title">BARAT</div>

    <div class="inshallah" lang="ar" dir="rtl">
        إن شاء الله
    </div>

    <div class="date-card">
        <div class="date">
            15 December 2026
        </div>

        <div class="time">
            Tuesday | 8:30 PM
        </div>
    </div>

    <div class="countdown-heading">
        COUNTING DOWN TO THE BIG DAY
    </div>

    <div class="countdown" id="countdown">
        <div class="time-box">
            <span class="time-number" id="days">--</span>
            <span class="time-unit">Days</span>
        </div>

        <div class="time-box">
            <span class="time-number" id="hours">--</span>
            <span class="time-unit">Hours</span>
        </div>

        <div class="time-box">
            <span class="time-number" id="minutes">--</span>
            <span class="time-unit">Minutes</span>
        </div>

        <div class="time-box">
            <span class="time-number" id="seconds">--</span>
            <span class="time-unit">Seconds</span>
        </div>
    </div>
</div>

<div class="section-card">
    <div class="venue-heading">THE VENUE</div>

    <div class="venue-name">
        Orient Banquet (Platinum)
    </div>

    <div class="venue-address">
        Karachi, Pakistan
    </div>

    <a class="map-link"
       href="https://www.google.com/maps/search/?api=1&query=Orient+Banquet+Platinum+Karachi"
       target="_blank"
       rel="noopener noreferrer">
       View Location
    </a>
</div>

<div class="section-card">
    <div class="section-title">
        Family Contacts
    </div>

    <div class="contacts">
        <div class="contact">
            <div class="contact-name">
                Farah Naz
            </div>

            <div class="contact-number">
                <a href="https://wa.me/923343636226" target="_blank">
                    +92 334 3636226
                </a>
            </div>
        </div>

        <div class="contact">
            <div class="contact-name">
                Musab Arif
            </div>

            <div class="contact-number">
                <a href="https://wa.me/923456174787" target="_blank">
                    +92 345 6174787
                </a>
            </div>
        </div>

        <div class="contact">
            <div class="contact-name">
                Ahsan Wasif
            </div>

            <div class="contact-number">
                <a href="https://wa.me/923312442692" target="_blank">
                    +92 331 2442692
                </a>
            </div>
        </div>
    </div>
</div>

<div class="section-card">
    <div class="section-title">
        Words of Blessings
    </div>

    <p class="section-description">
        Share your heartfelt wishes and prayers for the newlyweds.
        May Allah bless their journey together.
    </p>

    <div class="dua-options">
        <button
            class="dua-option"
            onclick="selectDua(this, 'بارك الله لكما')">
            بارك الله لكما
        </button>

        <button
            class="dua-option"
            onclick="selectDua(this, 'ہمیشہ خوش رہیں')">
            ہمیشہ خوش رہیں
        </button>

        <button
            class="dua-option"
            onclick="selectDua(this, 'جوڑی سلامت رہے، آمین')">
            جوڑی سلامت رہے، آمین
        </button>
    </div>

    <input
        id="duaInput"
        type="text"
        placeholder="Write your dua or wish here..."
        maxlength="180">

    <br>

    <button class="send-btn" onclick="sendDua()">
        Share Your Dua
    </button>

    <ul id="duaList"></ul>

    <p class="section-description"
       style="font-size:22px; margin-top:15px;">
        Your wishes will appear here during this visit.
    </p>
</div>

<div class="section-card">
    <div class="section-title">
        With Love &amp; Warm Wishes
    </div>

    <p class="section-description">
        For any assistance or inquiries, please feel free to reach out to our family hosts.
    </p>

    <a class="whatsapp-btn"
       href="https://wa.me/923343636226?text=Assalam-o-Alaikum%2C%20I%20would%20love%20to%20attend%20the%20Barat%20celebration%20of%20Durraiya%20and%20Hammad%20on%2015%20December%202026.%20Thank%20you%20for%20the%20invitation!"
       target="_blank"
       rel="noopener noreferrer">
       Confirm your Presence
    </a>
</div>

<div class="footer">
    WITH LOVE &amp; BLESSINGS
    <br>
    MR &amp; MRS. HAMMAD
</div>

</div>
</div>

<script>
const waxSeal = document.getElementById("waxSeal");
const envelopeIntro = document.getElementById("envelopeIntro");
const envelope = document.querySelector(".envelope");

let startPetalAnimation = () => {};

// Ask the Streamlit host to resize the iframe after the envelope opens.
// The initial envelope keeps its original full-screen height; only the
// invitation view is resized to its real content height.
function sendFrameHeight(height) {
    window.parent.postMessage(
        {
            isStreamlitMessage: true,
            type: "streamlit:setFrameHeight",
            height: Math.ceil(height)
        },
        "*"
    );
}

function getInvitationHeight() {
    return Math.max(
        document.documentElement.scrollHeight,
        document.body.scrollHeight
    );
}

function smoothlyFitInvitation() {
    const startHeight = window.innerHeight;
    const targetHeight = getInvitationHeight();
    const duration = 850;
    const startTime = performance.now();

    function animateResize(now) {
        const progress = Math.min((now - startTime) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const currentHeight = startHeight +
            (targetHeight - startHeight) * eased;

        sendFrameHeight(currentHeight);

        if (progress < 1) {
            requestAnimationFrame(animateResize);
        } else {
            sendFrameHeight(getInvitationHeight());
        }
    }

    requestAnimationFrame(animateResize);
}

waxSeal.addEventListener("click", function () {
    envelope.classList.add("open");

    setTimeout(function () {
        envelopeIntro.classList.add("hide");

        setTimeout(function () {
            envelopeIntro.remove();
            startPetalAnimation();

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

            smoothlyFitInvitation();

            if ("ResizeObserver" in window) {
                const page = document.querySelector(".page");

                if (page) {
                    const observer = new ResizeObserver(function () {
                        sendFrameHeight(getInvitationHeight());
                    });

                    observer.observe(page);
                }
            }
        }, 1000);
    }, 900);
});

const weddingDate =
    new Date("2026-12-15T20:30:00+05:00").getTime();

function updateCountdown() {
    const now = Date.now();
    const difference = weddingDate - now;

    if (difference <= 0) {
        document.getElementById("countdown").innerHTML =
            "<div class='section-title'>The Celebration Has Begun!</div>";
        return;
    }

    document.getElementById("days").textContent =
        Math.floor(difference / (1000 * 60 * 60 * 24));

    document.getElementById("hours").textContent =
        Math.floor((difference / (1000 * 60 * 60)) % 24);

    document.getElementById("minutes").textContent =
        Math.floor((difference / (1000 * 60)) % 60);

    document.getElementById("seconds").textContent =
        Math.floor((difference / 1000) % 60);
}

updateCountdown();
setInterval(updateCountdown, 1000);

function selectDua(button, message) {
    document.querySelectorAll(".dua-option").forEach(item => {
        item.classList.remove("selected");
    });

    button.classList.add("selected");
    document.getElementById("duaInput").value = message;
}

function sendDua() {
    const input = document.getElementById("duaInput");
    const message = input.value.trim();

    if (!message) {
        alert("Please write or select a dua first.");
        return;
    }

    const list = document.getElementById("duaList");
    const item = document.createElement("li");

    item.textContent = message;
    list.appendChild(item);

    input.value = "";

    document.querySelectorAll(".dua-option").forEach(button => {
        button.classList.remove("selected");
    });
}

(function () {
    const canvas = document.getElementById("fallingPetals");
    const ctx = canvas.getContext("2d");

    let petals = [];
    let width = 0;
    let height = 0;
    let started = false;

    const reducedMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    const colours = [
        "#8B2635",
        "#6F1D2A",
        "#A94F5C",
        "#B86B75",
        "#D58B91"
    ];

    function resize() {
        const ratio = Math.min(window.devicePixelRatio || 1, 2);

        width = window.innerWidth;
        height = window.innerHeight;

        canvas.width = width * ratio;
        canvas.height = height * ratio;

        ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

        const count = width < 600 ? 28 : 45;

        petals = Array.from({ length: count }, () => ({
            x: Math.random() * width,
            y: Math.random() * height,
            width: Math.random() * 5 + 5,
            length: Math.random() * 9 + 10,
            speed: Math.random() * 0.7 + 0.45,
            drift: Math.random() * 0.7 + 0.2,
            rotation: Math.random() * Math.PI * 2,
            rotationSpeed: (Math.random() - 0.5) * 0.018,
            phase: Math.random() * Math.PI * 2,
            opacity: Math.random() * 0.12 + 0.22,
            colour: colours[Math.floor(Math.random() * colours.length)]
        }));
    }

    function drawPetal(p) {
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate(p.rotation);
        ctx.globalAlpha = p.opacity;
        ctx.fillStyle = p.colour;
        ctx.shadowColor = "rgba(90, 20, 35, 0.12)";
        ctx.shadowBlur = 4;

        ctx.beginPath();
        ctx.moveTo(0, -p.length / 2);
        ctx.bezierCurveTo(
            p.width, -p.length / 3,
            p.width, p.length / 3,
            0, p.length / 2
        );
        ctx.bezierCurveTo(
            -p.width, p.length / 3,
            -p.width, -p.length / 3,
            0, -p.length / 2
        );
        ctx.fill();
        ctx.restore();
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        petals.forEach(p => {
            p.y += p.speed;
            p.x += Math.sin(p.phase) * p.drift;
            p.rotation += p.rotationSpeed;
            p.phase += 0.012;

            if (p.y > height + 25) {
                p.y = -25;
                p.x = Math.random() * width;
            }

            if (p.x > width + 20) p.x = -20;
            if (p.x < -20) p.x = width + 20;

            drawPetal(p);
        });

        requestAnimationFrame(animate);
    }

    resize();

    startPetalAnimation = function () {
        if (!started && !reducedMotion) {
            started = true;
            animate();
        }
    };

    window.addEventListener("resize", resize);
})();
</script>

</body>
</html>
"""

illustration_path = Path(__file__).with_name(
    "bride_groom_illustration.png"
)

if not illustration_path.exists():
    st.error(
        "Illustration image not found. "
        "Please keep bride_groom_illustration.png "
        "in the same folder as app.py."
    )
    st.stop()

illustration_b64 = base64.b64encode(
    illustration_path.read_bytes()
).decode("ascii")

html = html.replace(
    "__ILLUSTRATION_DATA__",
    illustration_b64
)

components.html(
    html,
    height=2900,
    scrolling=True
)
