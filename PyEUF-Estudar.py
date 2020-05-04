#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Tue Feb 26 19:18:22 2019

@author: diogo
"""
from __future__ import division;
import math as m;
import numpy as np;
import datetime;
import pandas as pd;
import subprocess
import signal
import os
import time

k = 0;
j = 0;

#São seis tópicos, então...

eletro = [[20091,[1,2,3]],[20092,[1,2,3]],[20101,[1,2,3]],[20102,[1,2,3]],[20111,[1,2,3]],[20121,[1,2,3]],[20122,[1,2,3]],[20131,[1,2,3]],[20132,[1,2,3]],[20141,[1,2,3]],[20142,[1,2,3]],[20151,[1,2,3]],[20152,[1,2,3]],[20161,[1,2,3]],[20162,[1,2,3]],[20171,[1,2,3]],[20172,[1,2,3]],[20181,[1,2,3]],[20182,[1,2,3]],[20191,[1,2,3]]];

fmoder = [[20091,[1,2,3]],[20092,[1,2,3]],[20101,[1,2,3]],[20102,[1,2,3]],[20111,[1,2,3]],[20121,[1,2,3]],[20122,[1,2,3]],[20131,[1,2,3]],[20132,[1,2,3]],[20141,[1,2,3]],[20142,[1,2,3]],[20151,[1,2,3]],[20152,[1,2,3]],[20161,[1,2,3]],[20162,[1,2,3]],[20171,[1,2,3]],[20172,[1,2,3]],[20181,[1,2,3]],[20182,[1,2,3]],[20191,[1,2,3]]];

termod = [[20091,[1,2,3]],[20092,[1,2,3]],[20101,[1,2,3]],[20102,[1,2,3]],[20111,[1,2,3]],[20121,[1,2,3]],[20122,[1,2,3]],[20131,[1,2,3]],[20132,[1,2,3]],[20141,[1,2,3]],[20142,[1,2,3]],[20151,[1,2,3]],[20152,[1,2,3]],[20161,[1,2,3]],[20162,[1,2,3]],[20171,[1,2,3]],[20172,[1,2,3]],[20181,[1,2,3]],[20182,[1,2,3]],[20191,[1,2,3]]];

mestat = [[20091,[1,2,3]],[20092,[1,2,3]],[20101,[1,2,3]],[20102,[1,2,3]],[20111,[1,2,3]],[20121,[1,2,3]],[20122,[1,2,3]],[20131,[1,2,3]],[20132,[1,2,3]],[20141,[1,2,3]],[20142,[1,2,3]],[20151,[1,2,3]],[20152,[1,2,3]],[20161,[1,2,3]],[20162,[1,2,3]],[20171,[1,2,3]],[20172,[1,2,3]],[20181,[1,2,3]],[20182,[1,2,3]],[20191,[1,2,3]]];

mclass = [[20091,[1,2,3]],[20092,[1,2,3]],[20101,[1,2,3]],[20102,[1,2,3]],[20111,[1,2,3]],[20121,[1,2,3]],[20122,[1,2,3]],[20131,[1,2,3]],[20132,[1,2,3]],[20141,[1,2,3]],[20142,[1,2,3]],[20151,[1,2,3]],[20152,[1,2,3]],[20161,[1,2,3]],[20162,[1,2,3]],[20171,[1,2,3]],[20172,[1,2,3]],[20181,[1,2,3]],[20182,[1,2,3]],[20191,[1,2,3]]];

mquant = [[20091,[1,2,3]],[20092,[1,2,3]],[20101,[1,2,3]],[20102,[1,2,3]],[20111,[1,2,3]],[20121,[1,2,3]],[20122,[1,2,3]],[20131,[1,2,3]],[20132,[1,2,3]],[20141,[1,2,3]],[20142,[1,2,3]],[20151,[1,2,3]],[20152,[1,2,3]],[20161,[1,2,3]],[20162,[1,2,3]],[20171,[1,2,3]],[20172,[1,2,3]],[20181,[1,2,3]],[20182,[1,2,3]],[20191,[1,2,3]]];

topicos = [eletro,fmoder,termod,mestat,mclass,mquant];

nomestopicos=['Teoria Eletromagnética','Física Moderna','Termodinâmica','Mecânica Estatística','Mecânica Clássica','Mecânica Quântica'];

while j < 1:
    if k == 0:
        input = raw_input('\nTens um save?[y/n]\n');

        if input == "y":

            save = raw_input('\nDigite o nome:\n');
            savename  = "save/" + save + ".csv"

            #Loop que analisa quais que vão ser as probabilidade de um tópico em um dia

            def ExpFun(t):
                return m.exp(-t*10**(-4));

            df1 = pd.read_csv(savename);
            #Esse comando exclui a coluna 'Unnamed' q aparece quando chamo o arquivo.
            df1.drop(df1.columns[df1.columns.str.contains('unnamed',case = False)],axis = 1);

            Day = df1.iloc[:,0].values;
            Hour = df1.iloc[:,1].values;
            MSecond = df1.iloc[:,2].values;
            Minute = df1.iloc[:,3].values;
            Month = df1.iloc[:,4].values;
            Question = df1.iloc[:,5].values;
            Second = df1.iloc[:,6].values;
            Topic = df1.iloc[:,7].values;
            Year = df1.iloc[:,8].values;

            w1 = 1/6;
            pesost = [w1,w1,w1,w1,w1,w1];

            #Escolhendo uma lista com os respectivos pesos
            now = datetime.datetime.now();

            i = 0;
            while i<len(Day):
            #    var3 = datetime.date(Year[-i],Month[-i],Day[-i]);
                dt = now - datetime.timedelta(days=120);
                dt1 = datetime.datetime(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,dt.microsecond);
                dt2 = datetime.datetime(Year[-i],Month[-i],Day[-i],Hour[-i],Minute[-i],Second[-i],MSecond[-i]);


                if dt1 < dt2:
                    dt3 = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)-dt2;
                    pesost[Topic[i]] = w1*(1-ExpFun(dt3.total_seconds()/60))/sum(pesost);
                    pesost = [x/sum(pesost) for x in pesost];
                    i = i+1;

                else:
                    i=i+1;

            var1 = np.random.choice(6,1, p = pesost);
            topico = topicos[var1[0]];

            #Peso estatístico inicial de cada questão

            numques = len(topico);
            w2 = 1/numques;

            i = 1;
            pesosq = [];

            while i<= numques:
                pesosq.append(w2);
                i = i+1;

            #Escolhendo um exercício com os respectivos pesos

            i = 0;
            while i<len(Day):
            #    var3 = datetime.date(Year[-i],Month[-i],Day[-i]);
                if Topic[i]==var1:
                    dt = now - datetime.timedelta(days=120);
                    dt1 = datetime.datetime(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,dt.microsecond);
                    dt2 = datetime.datetime(Year[-i],Month[-i],Day[-i],Hour[-i],Minute[-i],Second[-i],MSecond[-i]);

                    if dt1 < dt2:
                        dt3 = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)-dt2;
                        pesosq[Question[i]] = w2*(1-ExpFun(dt3.total_seconds()/60))/sum(pesosq);
                        pesosq = [x/sum(pesosq) for x in pesosq];
                        i = i+1;

                    else:
                        i=i+1;
                else:
                        i=i+1;

            pesosq = [x/sum(pesosq) for x in pesosq];

            var2 = np.random.choice(numques,1, p = pesosq);

            var3 = np.random.choice(3, 1);
            exercicio = topico[var2[0]][1][var3[0]];

            print("Vc tem que fazer o exercício " + str(exercicio) + " de " + str(nomestopicos[var1[0]]) + " da prova " + str(topico[var2[0]][0]) +".\n")

            #Salvando escolha
            df2 = pd.DataFrame({'Topic':[var1[0]],'Question':[var2[0]],'Year':[now.year],
                               'Month':[now.month],'Day':[now.day],'Hour':[now.hour],'Minute':[now.minute],'Second':[now.second],
                               'Microsecond':[now.microsecond]});

            df = pd.concat([df1,df2], ignore_index=True);
            df.to_csv(savename, index=False);

            again = raw_input('\nNovamente?[y/n]\n');

            if again == 'y':
                k=1;
            if again == 'n':
                j=1;

        if input == 'n':

            save = raw_input('\nDigite um nome para seu save:\n');
            savename  = "save/" + save + ".csv";

            w1 = 1/6;
            pesost = [w1,w1,w1,w1,w1,w1];

            var1 = np.random.choice(6,1, p = pesost);
            topico = topicos[var1[0]];
            #Peso estatístico inicial de cada questão

            numques = len(topico);
            w2 = 1/numques;

            i = 1;
            pesosq = [];

            while i<= numques:
                pesosq.append(w2);
                i = i+1;

            var2 = np.random.choice(numques,1, p = pesosq);

            var3 = np.random.choice(3,1);
            exercicio = topico[var2[0]][1][var3[0]];

            print("Vc tem que fazer o exercício " + str(exercicio) + " de " + str(nomestopicos[var1[0]]) + " da prova " + str(topico[var2[0]][0]) +".\n");

            time.sleep(5);

            filename="Provas Anteriores/" + str(topico[var2[0]][0]) + ".pdf"
            plot = subprocess.Popen("xreader '%s'" % filename, shell=True)

            prssgr = raw_input('\nProsseguir?[y/n]\n');

            input(str(topico[var2[0]][0]));
            os.killpg(os.getpgid(plot.pid), signal.SIGTERM);

            now = datetime.datetime.now();

            df = pd.DataFrame({'Topic':[var1[0]],'Question':[var2[0]],'Year':[now.year],
                               'Month':[now.month],'Day':[now.day],'Hour':[now.hour],'Minute':[now.minute],'Second':[now.second],
                               'Microsecond':[now.microsecond]});

            df.to_csv(savename, index=False);

            again = raw_input('\nNovamente?[y/n]\n');

            if again == 'y':
                k=1;
            if again == 'n':
                j=1;

    else:
        df1 = pd.read_csv(savename);
        #Esse comando exclui a coluna 'Unnamed' q aparece quando chamo o arquivo.
        df1.drop(df1.columns[df1.columns.str.contains('unnamed',case = False)],axis = 1);

        Day = df1.iloc[:,0].values;
        Hour = df1.iloc[:,1].values;
        MSecond = df1.iloc[:,2].values;
        Minute = df1.iloc[:,3].values;
        Month = df1.iloc[:,4].values;
        Question = df1.iloc[:,5].values;
        Second = df1.iloc[:,6].values;
        Topic = df1.iloc[:,7].values;
        Year = df1.iloc[:,8].values;

        w1 = 1/6;
        pesost = [w1,w1,w1,w1,w1,w1];

        #Escolhendo uma lista com os respectivos pesos
        now = datetime.datetime.now();

        i = 0;
        while i<len(Day):
            dt = now - datetime.timedelta(days=120);
            dt1 = datetime.datetime(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,dt.microsecond);
            dt2 = datetime.datetime(Year[-i],Month[-i],Day[-i],Hour[-i],Minute[-i],Second[-i],MSecond[-i]);


            if dt1 < dt2:
                dt3 = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)-dt2;
                pesost[Topic[i]] = w1*(1-ExpFun(dt3.total_seconds()/60))/sum(pesost);
                pesost = [x/sum(pesost) for x in pesost];
                i = i+1;

            else:
                i=i+1;

        var1 = np.random.choice(6,1, p = pesost);
        topico = topicos[var1[0]];

        #Peso estatístico inicial de cada questão

        numques = len(topico);
        w2 = 1/numques;

        i = 1;
        pesosq = [];

        while i<= numques:
            pesosq.append(w2);
            i = i+1;

            #Escolhendo um exercício com os respectivos pesos

        i = 0;
        while i<len(Day):
            if Topic[i]==var1:
                dt = now - datetime.timedelta(days=120);
                dt1 = datetime.datetime(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,dt.microsecond);
                dt2 = datetime.datetime(Year[-i],Month[-i],Day[-i],Hour[-i],Minute[-i],Second[-i],MSecond[-i]);

                if dt1 < dt2:
                    dt3 = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)-dt2;
                    pesosq[Question[i]] = w2*(1-ExpFun(dt3.total_seconds()/60))/sum(pesosq);
                    pesosq = [x/sum(pesosq) for x in pesosq];
                    i = i+1;

                else:
                    i=i+1;
            else:
                i=i+1;

        pesosq = [x/sum(pesosq) for x in pesosq];

        var2 = np.random.choice(numques,1, p = pesosq);

        var3 = np.random.choice(3,1);
        exercicio = topico[var2[0]][1][var3[0]];

        print("Vc tem que fazer o exercício " + str(exercicio) + " de " + str(nomestopicos[var1[0]]) + " da prova " + str(topico[var2[0]][0]) +".\n");
        #Salvando escolha
        df2 = pd.DataFrame({'Topic':[var1[0]],'Question':[var2[0]],'Year':[now.year],
                            'Month':[now.month],'Day':[now.day],'Hour':[now.hour],'Minute':[now.minute],'Second':[now.second],
                            'Microsecond':[now.microsecond]});

        df = pd.concat([df1,df2], ignore_index=True);
        df.to_csv(savename, index=False);

        again = raw_input('\nNovamente?[y/n]\n');
        if again == 'n':
            j=1;
