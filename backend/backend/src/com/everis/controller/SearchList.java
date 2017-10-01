package com.everis.controller;

import java.util.Vector;

/**
 * SearchList permite determinar el resultado de la busqueda almacenando los
 * matches de la misma.
 *
 * @author Jorge de Castro
 */
public class SearchList {

    private boolean search = false;
    private int matchCounter = 0;
    private Vector<SearchObject> searchVector = new Vector<SearchObject>();

    /**
     * setSearch permite determinar si la busqueda ha arrojado resultados o no
     *
     * @param state
     *            -> falso o verdadero dependiendo de si la busqueda ha obtenido
     *            resultados
     */
    public void setSearch(boolean state) {
        this.search = state;
    }

    /**
     * increaseCounter incrementa el matchCounter para determinar cuantos
     * resultados han encajado con la busqueda
     */
    public void increaseCounter() {
        this.matchCounter++;
    }

    /**
     * insertSearchObject introduce un objeto que encaje con la busqueda
     * (curriculum con su informacion de acceso) en la lista de SearchObject que
     * se devolvera en formato json como resultado final de la busqueda. De esta
     * manera se mostraran todos los matches con su informacion en el json
     * final. Ademas fija la busqueda como verdadera e incrementa el numero de
     * matches.
     *
     * @param object
     *            -> SearchObject donde se determina el id del curriculum, su
     *            acceso para descarga y su acceso para lectura del json
     *            parseado
     */
    public void insertSearchObject(SearchObject object) {
        getSearchVector().addElement(object);
        setSearch(true);
        increaseCounter();
    }

    /**
     * isSearch permite saber si la busqueda ha obtenido resultados o no
     *
     * @return true o false en funcion de si la busqueda ha obtenido resultados
     *         o no
     */
    public boolean isSearch() {
        return search;
    }

    /**
     * getMatchCounter devuelve el numero de matches de la busqueda
     *
     * @return devuelve un integer referente al numero de matches de la busqueda
     */
    public int getMatchCounter() {
        return matchCounter;
    }

    /**
     * getSearchVector devuelve el vector de resultados (objetos searchObject)
     *
     * @return vector de tipo SearchObject donde esta almacenada la informacion
     *         de los matches (curriculums con su informacion de acceso)
     */
    public Vector<SearchObject> getSearchVector() {
        return searchVector;
    }

}
