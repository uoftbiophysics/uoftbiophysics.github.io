---
layout: page
permalink: /contributors/
title: contributors
description: List of contributors and links to their github
nav: true
nav_order: 2
---

These are some of the wonderful folk who have made this blog possible. If you'd like to contribute, please feel free to reach out.

<div>
<!-- Team Section -->
    <section id="team" class="bg-light-gray">
        <div class="container">
            <div class="row" >
                <div class="col-lg-12 text-center">
                    <h2 class="section-heading">{{site.data[site.language].teamHeadline}}</h2>
                    <h3 class="section-subheading text-muted">{{site.data[site.language].teamSubheading}}</h3>
                </div>
            </div>
            <div class="row">
                {% for item in site.data.coauthors%}
                  {% assign member = item[1] %}
                  {% assign loopindex = forloop.index0 | modulo: 4 %}
                  {% if loopindex == 0 %}
                    {% if forloop.first == false %}
                  </div>
                      {% if forloop.last == false %}
                  <div class="row">
                      {% endif %}
                    {% endif %}
                  {% endif %}
                  <div class="col-sm-3">
                      <div class="team-member">
                          <center>
                          {% if member.github %}
                          <img class="rounded-circle profile img-responsive img-circle" src="https://avatars.githubusercontent.com/{{ member.github }}?s=200" alt="centered image">
                          <h4><a href="https://github.com/{{ member.github }}">{{ member.display_name }}</a></h4>
                          {% else %}
                          <i class="fa fa-user"></i>
                          <h4>{{ member.display_name }}</h4>
                          {% endif %}
                          <p class="text-muted"><i>{{ member.role }}</i></p>
                          {% if member.interests %}
                            {{site.data[site.language].interests}}:
                            <ul class="list-inline text-muted">
                                {% for interest in member.interests %}
                                  <li class="fa fa-angle-right">&nbsp;{{ interest }}</li>
                                {% endfor %}
                            </ul>
                          {% endif %}
                          </center>
                      </div>
                  </div>
                {% endfor %}
            </div>
        </div>
    </section>
</div>
