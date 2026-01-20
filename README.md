# GestorNotasAWS
## Miniproyecto  IAM para Lambda + DynamoDB

### Descripción
El siguiente proyecto consiste en un ejemplo de políticas de IAM establecidas para funciones Lambda que gestionan notas en una base de datos de DynamoDB.

### Servicios usados
- AWS Lambda Function
- AWS DynamoDB
- AWS IAM

## Objetivos

El objetivo del proyecto es aprender a diseñar y aplicar políticas IAM específicas para cada función Lambda, siguiendo el principio de privilegios mínimos y buenas prácticas de seguridad en AWS.


## Arquitectura general

(Imagen para el diagrama)

## Diseño IAM

Vamos a establecer un rol para cada función Lambda. Esto nos permite separar la responsabilidad por cada operación teniendo mayor control sobre nuestro proyecto de manera que este escrito bajo el protocolo "Least Privilege", que consiste en dar privilegios mínimos para lo que necesite cada servicio de AWS.

Además de ello necesitamos políticas para cada operación asegurándonos de que WriteNote solo pueda poner un ítem en DynamoDB en vez de hacer más cosas.

Cada rol incluirá dos partes:
- Una trust policy, que permite que Lambda asuma el rol
- Una permissions policy, que define que operación puede realizar en DynamoDB
