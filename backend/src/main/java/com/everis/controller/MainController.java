/**
 * REST service
 * 
 * @author: Jorge de Castro
 * @version: 17/03/2016/A
 * @see <a href = "https://bitbucket.org/jdecastroc/restcvparser" /> Bitbucket
 *      repository </a>
 */
package com.everis.controller;

import java.io.*;

import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.InputStreamResource;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

/**
 * La clase MainController es el controlador REST. Se encarga entonces de
 * realizar una búsqueda sobre los curriculums indexados en elastic search
 * ejecutando, en base a unos parámetros de búsqueda, el proceso curl del
 * servidor.
 * 
 */

@RestController
public class MainController {

	/**
	 * SearchCv se encarga de realizar la búsqueda sobre elastic search y
	 * devolver un json con la información pertinente.
	 * 
	 * @author Jorge de Castro
	 * @param id
	 *            -> (PathVariable) id del cv donde va a buscar la información.
	 *            "all" buscará en todos los indexados
	 * @param nombre
	 *            -> (RequestParam) nombre a buscar en los curriculums
	 * @param direccion
	 *            -> (RequestParam) dirección a buscar en los curriculums
	 * @param dni
	 *            -> (RequestParam) dni a buscar en los curriculums
	 * @param tecnologia
	 *            -> (RequestParam) tecnología a buscar en los curriculums
	 * @param empresa
	 *            -> (RequestParam) empresa a buscar en los curriculums
	 * @param idiomas
	 *            -> (RequestParam) idiomas a buscar en los curriculums
	 * @return json con la información de los curriculums que cumplen con los
	 *         parámetros de búsqueda
	 */
	@RequestMapping(value = "/buscador/{id}", method = RequestMethod.GET, produces = "application/json")
	@ResponseStatus(HttpStatus.OK)
	public @ResponseBody String searchCv(@PathVariable("id") String id, @RequestParam(value = "nombre") String nombre,
			@RequestParam(value = "direccion") String direccion, @RequestParam(value = "dni") String dni,
			@RequestParam(value = "tecnologia") String tecnologia, @RequestParam(value = "empresa") String empresa,
			@RequestParam(value = "idiomas") String idiomas) throws Exception {

		// Creamos el objeto search Object List donde almacenaremos las
		// busquedas que encajen con los parametros
		SearchList searchList = new SearchList();
		Gson gsonSearchList = new GsonBuilder().disableHtmlEscaping().setPrettyPrinting().create();

		StringBuilder processOutput = new StringBuilder();

		// Query para busqueda en elasticsearch
		String query = "{\"query\": {\"bool\": {\"should\": [{\"match\": {\"Datos Personales\": \"" + nombre
				+ "\"}},{\"match\": {\"Datos Personales\": \"" + direccion
				+ "\"}},{\"match\": {\"Datos Personales\": \"" + dni + "\"}},{\"match\": {\"Experiencia Laboral\": \""
				+ tecnologia + "\"}},{\"match\": {\"Formacion\": \"" + tecnologia
				+ "\"}},{\"match\": {\"Experiencia Laboral\": \"" + empresa + "\"}},{\"match\": {\"Idiomas\": \""
				+ idiomas + "\"}}]}}}";

		if (id.equals("all")) {
			System.out.println("Consulta: " + query);

			// Se arma el proceso que se va a ejecutar en el servidor
			ProcessBuilder processBuilder = new ProcessBuilder("curl", "-s", "-XGET",
					"http://51.255.202.84:9200/concurrente/cv/_search", "-d", query);

			processBuilder.redirectErrorStream(true);
			Process process = processBuilder.start();

			// Buffer para leer el output del proceso
			try (BufferedReader processOutputReader = new BufferedReader(
					new InputStreamReader(process.getInputStream()));) {
				String readLine;

				while ((readLine = processOutputReader.readLine()) != null) {
					processOutput.append(readLine + System.lineSeparator());
				}
				process.waitFor();
			}

		}

		// JSON parser para dar formato al texto y retornar un fichero json
		JsonParser parser = new JsonParser();
		JsonObject json = (JsonObject) parser.parse(processOutput.toString().trim());
		Gson gson = new GsonBuilder().setPrettyPrinting().create();
		String prettyJson = gson.toJson(json);

		System.out.println("Consulta finalizada con exito");

		// Json Parser to deserialize the object
		JsonParser parserReader = new JsonParser();
		JsonObject rootObj = parserReader.parse(prettyJson).getAsJsonObject();
		JsonArray idObj = rootObj.getAsJsonObject("hits").getAsJsonArray("hits");

		// Deserialize json to obtain the _id field
		for (JsonElement object : idObj) {

			JsonObject idObjString = object.getAsJsonObject();
			String idCv = idObjString.get("_id").getAsString();

			// Creamos el objeto search para almacenar la informacion de la
			// busqueda
			SearchObject searchObject = new SearchObject(idCv, "http://hugofs.com:8080/descargas/" + idCv,
					"http://hugofs.com:8080/curriculums/" + idCv);

			// Insertamos el objeto generado que encaja con la busqueda en la
			// lista final
			searchList.insertSearchObject(searchObject);

		}
		String searchListJson = gsonSearchList.toJson(searchList);
		return !searchListJson.equals("") ? searchListJson : "error";
	}

	/**
	 * searchCv envia une petición GET mediante el proceso curl del servidor al
	 * servicio del elasticSearch para consultar el json pedido por el cliente
	 * 
	 * @param id
	 *            -> id del curriculum del que se quiere obtener el json
	 *            indexado en elasticSearch
	 * @return json indexado en el elasticSearch
	 * @throws Exception
	 *             -> si el proceso curl no puede ejecutarse en el servidor
	 */
	@RequestMapping(value = "/curriculums/{id}", method = RequestMethod.GET, produces = "application/json")
	@ResponseStatus(HttpStatus.OK)
	public @ResponseBody String getCv(@PathVariable("id") String id) throws Exception {

		StringBuilder processOutput = new StringBuilder();

		String address = "http://51.255.202.84:9200/concurrente/cv/" + id;

		if (!id.equals("")) {
			System.out.println("Consulta: http://51.255.202.84:9200/concurrente/cv/" + id);

			// Se arma el proceso que se va a ejecutar en el servidor
			ProcessBuilder processBuilder = new ProcessBuilder("curl", "-s", "-XGET", address.trim());

			processBuilder.redirectErrorStream(true);
			Process process = processBuilder.start();

			// Buffer para leer el output del proceso
			try (BufferedReader processOutputReader = new BufferedReader(
					new InputStreamReader(process.getInputStream()));) {
				String readLine;

				while ((readLine = processOutputReader.readLine()) != null) {
					processOutput.append(readLine + System.lineSeparator());
				}
				process.waitFor();
			}
		}

		// JSON parser para dar formato al texto y retornar un fichero json
		JsonParser parser = new JsonParser();
		JsonObject json = (JsonObject) parser.parse(processOutput.toString().trim());
		Gson gson = new GsonBuilder().setPrettyPrinting().create();
		String prettyJson = gson.toJson(json);

		System.out.println("Consulta finalizada con exito");

		return !prettyJson.equals("") ? prettyJson : "error";
	}

	/**
	 * downloadFile se encarga de descargar el fichero del repositorio de
	 * curriculums en el cliente pasandole el nombre del curriculum que se desea
	 * descargar
	 * 
	 * @param fileName
	 *            -> nombre del curriculum a descargar
	 * @return fichero del curriculum
	 * @throws IOException
	 *             -> si no se encuentra el curriculum en el repositorio
	 */
	@RequestMapping(value = "/descargas/{file_name}", method = RequestMethod.GET)
	public @ResponseBody ResponseEntity<InputStreamResource> downloadFile(@PathVariable("file_name") String fileName)
			throws IOException {

		// TODO Add within pdf return content type HTML and DOC. Check it with
		// regex.
		ClassPathResource pdfFile = new ClassPathResource("cvReal/" + fileName + ".pdf");

		return ResponseEntity.ok().contentLength(pdfFile.contentLength())
				.contentType(MediaType.parseMediaType("application/pdf"))
				.body(new InputStreamResource(pdfFile.getInputStream()));
	}

    @RequestMapping(value = "/subir", method = RequestMethod.POST)
    public @ResponseBody String uploadFile(@RequestParam("name") String name, @RequestParam("file") MultipartFile file) {
        if (!file.isEmpty()) {
            try {
                 byte[] bytes = file.getBytes();
 
                // Creating the directory to store file
                String rootPath = System.getProperty("user.dir");  // Current directory
                File dir = new File(rootPath + File.separator + "src" + File.separator + "main" + File.separator + "resources" + File.separator + "cvReal");
                if (!dir.exists())
                    dir.mkdirs();
 
                // Create the file on server
                File serverFile = new File(dir.getAbsolutePath()
                        + File.separator + name);
                BufferedOutputStream stream = new BufferedOutputStream(
                        new FileOutputStream(serverFile));
                stream.write(bytes);
                stream.close();
                return "You successfully uploaded file=" + name;


            } catch (Exception e) {
                return "You failed to upload " + name + " => " + e.getMessage();
            }
        } else {
            return "You failed to upload " + name
                    + " because the file was empty.";
        }
    }
}
