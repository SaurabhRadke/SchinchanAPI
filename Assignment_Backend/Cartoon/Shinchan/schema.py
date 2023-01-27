import graphene
from graphene_django import DjangoObjectType
from .models import SchinchanSeries,ShinchanMovies

class MoviesType(DjangoObjectType): # Serializer For Shinchan Movies
    class Meta:
        model=ShinchanMovies
        fields=("id","Title","Year","IMDB","Cover","Duration")
class SeriesType(DjangoObjectType):  # Serializers for Shinchan Series
    class Meta:
        model=SchinchanSeries
        fields=("id","Season","Episodes","Relise_Year")

# ALl queries Class
class Query(graphene.ObjectType):
    all_movies=graphene.List(MoviesType)  # GET Compelete data of all Shichan Movies 
    all_series=graphene.List(SeriesType)  # GET Complete data of all Shinchan Web Series
    single_movie=graphene.Field(MoviesType,id=graphene.Int())
    single_series=graphene.Field(SeriesType,id=graphene.Int())

    # Function to get all Movie data
    def resolve_all_movies(root,info):  
        return ShinchanMovies.objects.all()

    # Function to get all Series Data  
    def resolve_all_series(root,info):
        return SchinchanSeries.objects.all()

    # Function to get Movies data of particular ID
    def resolve_single_movie(root,info,id):
        return ShinchanMovies.objects.get(pk=id)

    # Function to get Series data of particular ID
    def resolve_single_series(root,info,id):
        return SchinchanSeries.objects.get(pk=id)


#[PUT Request] /Update Mutation in Schinchan Movie data
class MovieMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        Title = graphene.String(required=True)

    movie=graphene.Field(MoviesType)

    @classmethod
    def mutate(cls,root,info,Title,id):
        movie=ShinchanMovies.objects.get(id=id)
        movie.Title=Title
        movie.save()
        return MovieMutation(movie=movie)


 # PUT request for Schinchan  Series 
class SeriesMutationPUT(graphene.Mutation):
    seriess=graphene.Field(SeriesType)
    class Arguments:
        id = graphene.ID()
        Episod = graphene.Int(required=True)

    def mutate(self,info,Episod,id):
        se=SchinchanSeries.objects.get(id=id)
        se.Episodes=Episod
        se.save()
        return SeriesMutationPUT(seriess=se)

#[DELETE MEthod] /Delete Metaion to delete an element
class MovieMutationdel(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    movie=graphene.Field(MoviesType)

    @classmethod
    def mutate(cls,root,info,id):
        movie=ShinchanMovies.objects.get(id=id)
        movie.delete()
        return MovieMutationdel(movie=movie)


# DELETE Request to Delete data from Schinachan Series
class SeriesMutationDel(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    series=graphene.Field(SeriesType)

    @classmethod
    def mutate(cls,root,info,id):
        seri=SchinchanSeries.objects.get(id=id)
        seri.delete()
        return SeriesMutationDel(series=seri)


# POST Request to add new season in Series
class SeriesMutation(graphene.Mutation):

    class Arguments:
        Season=graphene.Int(required= True)
        Episodes=graphene.Int(required= True)
        Relise_Year=graphene.Int(required=True)
    
    series=graphene.Field(SeriesType)
    @classmethod
    def mutate(cls,root,info,Season,Episodes,Relise_Year):
        series = SchinchanSeries(Season=Season,Episodes=Episodes,Relise_Year=Relise_Year)
        series.save()
        return SeriesMutation(series=series)


# POST Request to add new Movie in Series
class MoviesMutationAdd(graphene.Mutation):
    mov=graphene.Field(MoviesType)
    class Arguments:
        Title=graphene.String()
        Year=graphene.Date()
        IMDB=graphene.Float()
        Duration=graphene.Int()
        Cover=graphene.String()
    
    def mutate(self,info,Title,Year,IMDB,Duration,Cover):
        movie = ShinchanMovies(Title=Title,Year=Year,IMDB=IMDB,Duration=Duration,Cover=Cover)
        movie.save()
        return MoviesMutationAdd(mov=movie)

class Mutation(graphene.ObjectType):
    add_series = SeriesMutation.Field()
    delete_movies = MovieMutationdel.Field()
    update_movies = MovieMutation.Field()
    add_movies = MoviesMutationAdd.Field()
    update_series =SeriesMutationPUT.Field()
    delete_series=SeriesMutationDel.Field()

    

schema=graphene.Schema(query=Query, mutation=Mutation)

