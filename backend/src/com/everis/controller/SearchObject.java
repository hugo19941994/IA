package com.everis.controller;

/**
 * SearchObject contiene la informacion referente a cada match de la busqueda.
 * Almacena la id del curriculum, el enlace para su descarga y el enlace para
 * obtener el json parseado referente al mismo.
 * 
 * @author Jorge de Castro
 *
 */
public class SearchObject {

	private String curriculumId;
	private int curriculumScore;
	private String downloadCvLink;
	private String parsedCvLink;

	/**
	 * Constructor principal de la clase. Fija la id del curriculum, el enlace
	 * de descarga y el enlace del json parseado
	 * 
	 * @param id
	 *            -> id del curriculum del match
	 * @param downloadLink
	 *            -> enlace de descarga del curriculum del match
	 * @param parsedLink
	 *            -> enlace al json indexado en el elasticSearch del curriculum
	 *            del match
	 */
	public SearchObject(String id, int score, String downloadLink, String parsedLink) {
		this.setCurriculumId(id);
		this.setCurriculumScore(score);
		this.setDownloadCvLink(downloadLink);
		this.setParsedCvLink(parsedLink);
	}

	/**
	 * getCurriculumId devuelve el id del curriculum del match
	 * 
	 * @return string con el id del curriculum del match
	 */
	public String getCurriculumId() {
		return curriculumId;
	}
	
	/**
	 * getCurriculumScore devuelve el score del hit para comprobar el grado de match del hit
	 * 
	 * @return string con el score del match
	 */
	public int getCurriculumScore() {
		return curriculumScore;
	}

	/**
	 * getDownloadCvLink devuelve el enlace de descarga del curriculum del match
	 * 
	 * @return string con el enlace de descarga del curriculum del match
	 */
	public String getDownloadCvLink() {
		return downloadCvLink;
	}

	/**
	 * getParsedCvLink devuelve el enlace al curriculum indexado en el elastic search
	 * 
	 * @return string con el enlace al curriculum indexado en el elastic search
	 */
	public String getParsedCvLink() {
		return parsedCvLink;
	}

	/**
	 * setCurriculumId Fija el id del curriculum del match
	 * 
	 * @param curriculumId -> id del curriculum del match
	 */
	public void setCurriculumId(String curriculumId) {
		this.curriculumId = curriculumId;
	}
	
	/**
	 * setCurriculumId Fija el score del curriculum del match
	 * 
	 * @param curriculumScore -> score del curriculum del match
	 */
	public void setCurriculumScore(int score) {
		this.curriculumScore = score;
	}

	/**
	 * setDownloadCvLink Fija el enlace de descarga del curriculum del match
	 * 
	 * @param downloadCvLink -> string del enlace de descarga del curriculum del match
	 */
	public void setDownloadCvLink(String downloadCvLink) {
		this.downloadCvLink = downloadCvLink;
	}

	/**
	 * setParsedCvLink Fija el enlace al json indexado en el elasticSearch referente al curriculum del match
	 * 
	 * @param parsedCvLink -> string del enlace al json indexado en el ES
	 */
	public void setParsedCvLink(String parsedCvLink) {
		this.parsedCvLink = parsedCvLink;
	}
}
